package hex.modelselection;

import org.junit.Test;
import org.junit.runner.RunWith;
import water.DKV;
import water.Key;
import water.Scope;
import water.TestUtil;
import water.fvec.Frame;
import water.runner.CloudSize;
import water.runner.H2ORunner;

import static hex.glm.GLMModel.GLMParameters.Family.gaussian;
import static hex.modelselection.ModelSelectionModel.ModelSelectionParameters.Mode.allsubsets;
import static hex.modelselection.ModelSelectionModel.ModelSelectionParameters.Mode.backward;

@RunWith(H2ORunner.class)
@CloudSize(1)
public class BackwardSelectionTests extends TestUtil {
    @Test
    public void testGaussian() {
        Scope.enter();
        try {
            Frame origF = Scope.track(parseTestFile("smalldata/glm_test/gaussian_20cols_10000Rows.csv"));
            Frame trainF = new Frame(Key.make());
            String[] predNames = origF.names();
            int[] coefInd = new int[]{0, 2, 4, 6, 8, 10, 12, 14, 16, 18};
            for (int index : coefInd)
                trainF.add(predNames[index], origF.vec(index));
            trainF.add("C21", origF.vec("C21"));
            DKV.put(trainF);
            Scope.track(trainF);
            ModelSelectionModel.ModelSelectionParameters parms = new ModelSelectionModel.ModelSelectionParameters();
            parms._response_column = "C21";
            parms._family = gaussian;
            parms._min_predictor_number = 3;
            parms._train = trainF._key;
            parms._mode = backward;
            ModelSelectionModel modelAllSubsets = new hex.modelselection.ModelSelection(parms).trainModel().get();
            Scope.track_generic(modelAllSubsets);
        } finally {
            Scope.exit();
        }
    }
}
