package water.rapids.ast.prims.time;

import org.joda.time.DateTimeZone;
import org.joda.time.IllegalFieldValueException;
import org.joda.time.MutableDateTime;
import water.Key;
import water.MRTask;
import water.fvec.Chunk;
import water.fvec.Frame;
import water.fvec.NewChunk;
import water.fvec.Vec;
import water.rapids.Val;
import water.rapids.ast.AstBuiltin;
import water.rapids.vals.ValFrame;
import water.util.ArrayUtils;

import java.util.ArrayList;


/**
 * Convert year, month, day, hour, minute, sec, msec to Unix epoch time
 * (in milliseconds).
 *
 * This is a replacement for {@code AstMktime} class.
 */
public class AstMoment extends AstBuiltin<AstMoment> {

  @Override public int nargs() {
    return 8;
  }

  public String[] args() {
    return new String[]{"yr", "mo", "dy", "hr", "mi", "se", "ms"};
  }

  @Override public String str() {
    return "moment";
  }


  @Override
  public ValFrame apply(Val[] args) {

    // Parse the input arguments, verifying their validity.
    boolean naResult = false;
    long numRows = -1;
    int[] timeparts = new int[7];
    ArrayList<Integer> chunksmap = new ArrayList<>(7);
    ArrayList<Vec> timevecs = new ArrayList<>(7);
    for (int i = 0; i < 7; i++) {
      Val vi = args[i + 1];
      if (vi.isFrame()) {
        Frame fr = vi.getFrame();
        if (fr.numCols() != 1)
          throw new IllegalArgumentException("Argument " + i + " is a frame with " + fr.numCols() + " columns");
        if (!fr.vec(0).isNumeric())
          throw new IllegalArgumentException("Argument " + i + " is not a numeric column");
        if (fr.numRows() == 0)
          throw new IllegalArgumentException("Column " + i + " has 0 rows");
        if (fr.numRows() == 1) {
          double d = fr.vec(0).at(0);
          if (Double.isNaN(d))
            naResult = true;
          else
            timeparts[i] = (int) d;
        } else {
          if (numRows == -1)
            numRows = fr.numRows();
          if (fr.numRows() != numRows)
            throw new IllegalArgumentException("Incompatible vec " + i + " having " + fr.numRows() + " rows, whereas " +
                                               "other vecs have " + numRows + " rows.");
          timevecs.add(fr.vec(0));
          chunksmap.add(i);
        }
      } else if (vi.isNum()){
        double d = vi.getNum();
        if (Double.isNaN(d))
          naResult = true;
        else
          timeparts[i] = (int) d;
      } else {
        throw new IllegalArgumentException("Argument " + i + " is neither a number nor a frame");
      }
    }

    // If all arguments are scalars, return a 1x1 frame
    if (timevecs.isEmpty()) {
      double val = Double.NaN;
      if (!naResult) {
        try {
          val = new MutableDateTime(timeparts[0], timeparts[1], timeparts[2], timeparts[3], timeparts[4],
                                    timeparts[5], timeparts[6], DateTimeZone.UTC).getMillis();
        } catch (IllegalFieldValueException ignored) {}
      }
      return make1x1Frame(val);
    }

    // Some arguments are vecs -- create a frame of the same size
    Vec[] vecs = timevecs.toArray(new Vec[timevecs.size()]);
    int[] cm = ArrayUtils.unbox(chunksmap);
    Frame fr = new SetTimeTask(timeparts, cm, naResult)
        .doAll(Vec.T_TIME, vecs)
        .outputFrame(Key.<Frame>make(), new String[]{"time"}, null);

    return new ValFrame(fr);
  }

  private ValFrame make1x1Frame(double val) {
    Vec v = Vec.makeTimeVec(new double[]{val}, null);
    Frame f = new Frame(new String[]{"time"}, new Vec[]{v});
    return new ValFrame(f);
  }


  private static class SetTimeTask extends MRTask<SetTimeTask> {
    private int[] tp;
    private int[] cm;
    private boolean na;

    /**
     * @param timeparts is the array of [year, month, day, hrs, mins, secs, ms]
     *                  for all constant parts of the date;
     * @param chunksmap is a mapping between chunks indices and the timeparts
     *                  array. For example, if {@code chunksmap = [1, 2]},
     *                  then the first chunk describes the "month" part of the
     *                  date, and the second chunk the "day" part.
     */
    public SetTimeTask(int[] timeparts, int[] chunksmap, boolean naResult) {
      tp = timeparts;
      cm = chunksmap;
      na = naResult;
    }

    @Override public void map(Chunk[] chks, NewChunk nc) {
      int nVecs = cm.length;
      assert chks.length == nVecs;
      MutableDateTime dt = new MutableDateTime(0, DateTimeZone.UTC);
      int nChunkRows = chks[0]._len;
      if (na) {
        for (int i = 0; i < nChunkRows; i++) {
          nc.addNum(Double.NaN);
        }
      } else {
        BYROW:
        for (int i = 0; i < nChunkRows; i++) {
          for (int j = 0; j < nVecs; j++) {
            double d = chks[j].atd(i);
            if (Double.isNaN(d)) {
              nc.addNum(Double.NaN);
              continue BYROW;
            }
            tp[cm[j]] = (int) d;
          }
          dt.setDateTime(tp[0], tp[1], tp[2], tp[3], tp[4], tp[5], tp[6]);
          nc.addNum(dt.getMillis());
        }
      }
    }
  }
}
