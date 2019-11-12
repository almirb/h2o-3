#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# This file is auto-generated by h2o-3/h2o-bindings/bin/gen_python.py
# Copyright 2016 H2O.ai;  Apache License Version 2.0 (see LICENSE for details)
#
from __future__ import absolute_import, division, print_function, unicode_literals

from h2o.estimators.estimator_base import H2OEstimator
from h2o.exceptions import H2OValueError
from h2o.frame import H2OFrame
from h2o.utils.typechecks import assert_is_type, Enum, numeric
import h2o


class H2OTargetEncoderEstimator(H2OEstimator):
    """
    TargetEncoder

    """

    algo = "targetencoder"
    param_names = {"blending", "k", "f", "data_leakage_handling", "model_id", "ignored_columns", "training_frame",
                   "fold_column", "response_column"}

    def __init__(self, **kwargs):
        super(H2OTargetEncoderEstimator, self).__init__()
        self._parms = {}
        for pname, pvalue in kwargs.items():
            if pname == 'model_id':
                self._id = pvalue
                self._parms["model_id"] = pvalue
            elif pname in self.param_names:
                # Using setattr(...) will invoke type-checking of the arguments
                setattr(self, pname, pvalue)
            else:
                raise H2OValueError("Unknown parameter %s = %r" % (pname, pvalue))

    @property
    def blending(self):
        """
        Blending enabled/disabled

        Type: ``bool``  (default: ``False``).

        :examples:

        >>> titanic = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/gbm_test/titanic.csv")
        >>> predictors = ["home.dest", "cabin", "embarked"]
        >>> response = "survived"
        >>> titanic["survived"] = titanic["survived"].asfactor()
        >>> fold_col = "kfold_column"
        >>> titanic[fold_col] = titanic.kfold_column(n_folds=5, seed=1234)
        >>> titanic_te = H2OTargetEncoderEstimator(k=35,
        ...                                        f=25,
        ...                                        blending=True)
        >>> titanic_te.train(x=predictors,
        ...                  y=response,
        ...                  training_frame=titanic)
        >>> titanic_te
        """
        return self._parms.get("blending")

    @blending.setter
    def blending(self, blending):
        assert_is_type(blending, None, bool)
        self._parms["blending"] = blending


    @property
    def k(self):
        """
        Inflection point. Used for blending (if enabled). Blending is to be enabled separately using the 'blending'
        parameter.

        Type: ``float``  (default: ``10``).

        :examples:

        >>> titanic = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/gbm_test/titanic.csv")
        >>> predictors = ["home.dest", "cabin", "embarked"]
        >>> response = "survived"
        >>> titanic["survived"] = titanic["survived"].asfactor()
        >>> fold_col = "kfold_column"
        >>> titanic[fold_col] = titanic.kfold_column(n_folds=5, seed=1234)
        >>> titanic_te = H2OTargetEncoderEstimator(k=35,
        ...                                        f=25,
        ...                                        blending=True)
        >>> titanic_te.train(x=predictors,
        ...                  y=response,
        ...                  training_frame=titanic)
        >>> titanic_te
        """
        return self._parms.get("k")

    @k.setter
    def k(self, k):
        assert_is_type(k, None, numeric)
        self._parms["k"] = k


    @property
    def f(self):
        """
        Smoothing. Used for blending (if enabled). Blending is to be enabled separately using the 'blending' parameter.

        Type: ``float``  (default: ``20``).

        :examples:

        >>> titanic = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/gbm_test/titanic.csv")
        >>> predictors = ["home.dest", "cabin", "embarked"]
        >>> response = "survived"
        >>> titanic["survived"] = titanic["survived"].asfactor()
        >>> fold_col = "kfold_column"
        >>> titanic[fold_col] = titanic.kfold_column(n_folds=5, seed=1234)
        >>> titanic_te = H2OTargetEncoderEstimator(k=35,
        ...                                        f=25,
        ...                                        blending=True)
        >>> titanic_te.train(x=predictors,
        ...                  y=response,
        ...                  training_frame=titanic)
        >>> titanic_te
        """
        return self._parms.get("f")

    @f.setter
    def f(self, f):
        assert_is_type(f, None, numeric)
        self._parms["f"] = f


    @property
    def data_leakage_handling(self):
        """
        Data leakage handling strategy.

        One of: ``"none"``, ``"k_fold"``, ``"leave_one_out"``  (default: ``"none"``).

        :examples:

        >>> titanic = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/gbm_test/titanic.csv")
        >>> predictors = ["home.dest", "cabin", "embarked"]
        >>> response = "survived"
        >>> titanic["survived"] = titanic["survived"].asfactor()
        >>> fold_col = "kfold_column"
        >>> titanic[fold_col] = titanic.kfold_column(n_folds=5, seed=1234)
        >>> titanic_te = H2OTargetEncoderEstimator(k=35,
        ...                                        f=25,
        ...                                        data_leakage_handling="k_fold",
        ...                                        blending=True)
        >>> titanic_te.train(x=predictors,
        ...                  y=response,
        ...                  training_frame=titanic)
        >>> titanic_te
        """
        return self._parms.get("data_leakage_handling")

    @data_leakage_handling.setter
    def data_leakage_handling(self, data_leakage_handling):
        assert_is_type(data_leakage_handling, None, Enum("none", "k_fold", "leave_one_out"))
        self._parms["data_leakage_handling"] = data_leakage_handling


    @property
    def ignored_columns(self):
        """
        Names of columns to ignore for training.

        Type: ``List[str]``.
        """
        return self._parms.get("ignored_columns")

    @ignored_columns.setter
    def ignored_columns(self, ignored_columns):
        assert_is_type(ignored_columns, None, [str])
        self._parms["ignored_columns"] = ignored_columns


    @property
    def training_frame(self):
        """
        Id of the training data frame.

        Type: ``H2OFrame``.

        :examples:

        >>> titanic = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/gbm_test/titanic.csv")
        >>> predictors = ["home.dest", "cabin", "embarked"]
        >>> response = "survived"
        >>> titanic["survived"] = titanic["survived"].asfactor()
        >>> fold_col = "kfold_column"
        >>> titanic[fold_col] = titanic.kfold_column(n_folds=5, seed=1234)
        >>> titanic_te = H2OTargetEncoderEstimator(k=35,
        ...                                        f=25,
        ...                                        blending=True)
        >>> titanic_te.train(x=predictors,
        ...                  y=response,
        ...                  training_frame=titanic)
        >>> titanic_te
        """
        return self._parms.get("training_frame")

    @training_frame.setter
    def training_frame(self, training_frame):
        self._parms["training_frame"] = H2OFrame._validate(training_frame, 'training_frame')


    @property
    def fold_column(self):
        """
        Column with cross-validation fold index assignment per observation.

        Type: ``str``.

        :examples:

        >>> titanic = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/gbm_test/titanic.csv")
        >>> predictors = ["home.dest", "cabin", "embarked"]
        >>> response = "survived"
        >>> titanic["survived"] = titanic["survived"].asfactor()
        >>> fold_col = "kfold_column"
        >>> titanic[fold_col] = titanic.kfold_column(n_folds=5, seed=1234)
        >>> titanic_te = H2OTargetEncoderEstimator(k=35,
        ...                                        f=25,
        ...                                        blending=True)
        >>> titanic_te.train(x=predictors,
        ...                  y=response,
        ...                  training_frame=titanic)
        >>> titanic_te
        """
        return self._parms.get("fold_column")

    @fold_column.setter
    def fold_column(self, fold_column):
        assert_is_type(fold_column, None, str)
        self._parms["fold_column"] = fold_column


    @property
    def response_column(self):
        """
        Response variable column.

        Type: ``str``.
        """
        return self._parms.get("response_column")

    @response_column.setter
    def response_column(self, response_column):
        assert_is_type(response_column, None, str)
        self._parms["response_column"] = response_column


    def transform(self, frame, data_leakage_handling="None", noise=-1, seed=-1):
        """

        Apply transformation to `te_columns` based on the encoding maps generated during `train()` method call.

        :param H2OFrame frame: to which frame we are applying target encoding transformations.
        :param str data_leakage_handling: Supported options:

        1) "k_fold" - encodings for a fold are generated based on out-of-fold data.
        2) "leave_one_out" - leave one out. Current row's response value is subtracted from the pre-calculated per-level frequencies.
        3) "none" - we do not holdout anything. Using whole frame for training

        :param float noise: the amount of random noise added to the target encoding.  This helps prevent overfitting. Defaults to 0.01 * range of y.
        :param int seed: a random seed used to generate draws from the uniform distribution for random noise. Defaults to -1.

        :example:
        >>> titanic = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/gbm_test/titanic.csv")
        >>> predictors = ["home.dest", "cabin", "embarked"]
        >>> response = "survived"
        >>> titanic[response] = titanic[response].asfactor()
        >>> fold_col = "kfold_column"
        >>> titanic[fold_col] = titanic.kfold_column(n_folds=5, seed=1234)
        >>> titanic_te = H2OTargetEncoderEstimator(k=35,
        ...                                        f=25,
        ...                                        data_leakage_handling="leave_one_out",
        ...                                        blending=True)
        >>> titanic_te.train(x=predictors,
        ...                  y=response,
        ...                  training_frame=titanic)
        >>> transformed = titanic_te.transform(frame=titanic,
        ...                                    data_leakage_handling="leave_one_out",
        ...                                    seed=1234)
        """
        output = h2o.api("GET /3/TargetEncoderTransform", data={'model': self.model_id, 'frame': frame.key,
                                                                'data_leakage_handling': data_leakage_handling,
                                                                'noise': noise,
                                                                'seed': seed})
        return h2o.get_frame(output["name"])
