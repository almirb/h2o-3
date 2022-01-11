# coding=utf-8
import sys
sys.path.insert(1,"../../")
import h2o
from tests import pyunit_utils
import pandas as pd
import locale

def encofrce_utf8_encoding():
    orig_locale = locale.getlocale()
    all_rows = pd.read_csv(pyunit_utils.locate("smalldata/gbm_test/titanic.csv"))
    all_rows.at[0,0] = "�"
    try:
        locale.setlocale(locale.LC_ALL, 'en_US.ISO8859-1')
        # this reproduces the encoding error when certain codec can't encode certain character 
        h2o.H2OFrame(all_rows)
        locale.setlocale(locale.LC_ALL, orig_locale)
    except locale.Error:
        print("Unsupported locale setting, cannot test!")
        print("List of supported locales: ")
        print(locale.locale_alias)
        raise locale.Error("Unsupported locale setting, cannot test!") 
        
    
if __name__ == "__main__":
    pyunit_utils.standalone_test(encofrce_utf8_encoding)
else:
    encofrce_utf8_encoding()

