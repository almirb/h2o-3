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


class H2OGeneralizedLowRankEstimator(H2OEstimator):
    """
    Generalized Low Rank Modeling

    Builds a generalized low rank model of a H2O dataset.
    """

    algo = "glrm"
    param_names = {"model_id", "training_frame", "validation_frame", "ignored_columns", "ignore_const_cols",
                   "score_each_iteration", "loading_name", "transform", "k", "loss", "loss_by_col", "loss_by_col_idx",
                   "multi_loss", "period", "regularization_x", "regularization_y", "gamma_x", "gamma_y",
                   "max_iterations", "max_updates", "init_step_size", "min_step_size", "seed", "init", "svd_method",
                   "user_y", "user_x", "expand_user_y", "impute_original", "recover_svd", "max_runtime_secs",
                   "export_checkpoints_dir"}

    def __init__(self, **kwargs):
        super(H2OGeneralizedLowRankEstimator, self).__init__()
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
    def training_frame(self):
        """
        Id of the training data frame.

        Type: ``H2OFrame``.

        :examples:

        >>> prostate = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/prostate/prostate_cat.csv")
        >>> prostate[0] = prostate[0].asnumeric()
        >>> prostate[4] = prostate[4].asnumeric()
        >>> pros_glrm = H2OGeneralizedLowRankEstimator(k=5,
        ...                                            seed=1234)
        >>> pros_glrm.train(x=prostate.names, training_frame=prostate)
        >>> pros_glrm.show()
        """
        return self._parms.get("training_frame")

    @training_frame.setter
    def training_frame(self, training_frame):
        self._parms["training_frame"] = H2OFrame._validate(training_frame, 'training_frame')


    @property
    def validation_frame(self):
        """
        Id of the validation data frame.

        Type: ``H2OFrame``.

        :examples:

        >>> iris = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/iris/iris_wheader.csv")
        >>> iris_glrm = H2OGeneralizedLowRankEstimator(k=3,
        ...                                            loss="quadratic",
        ...                                            gamma_x=0.5,
        ...                                            gamma_y=0.5,
        ...                                            transform="standardize")
        >>> iris_glrm.train(x=iris.names,
        ...                 training_frame=iris,
        ...                 validation_frame=iris)
        >>> iris_glrm.show()
        """
        return self._parms.get("validation_frame")

    @validation_frame.setter
    def validation_frame(self, validation_frame):
        self._parms["validation_frame"] = H2OFrame._validate(validation_frame, 'validation_frame')


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
    def ignore_const_cols(self):
        """
        Ignore constant columns.

        Type: ``bool``  (default: ``True``).

        :examples:

        >>> iris = h2o.import_file("http://h2o-public-test-data.s3.amazonaws.com/smalldata/iris/iris_wheader.csv")
        >>> iris_glrm = H2OGeneralizedLowRankEstimator(k=3,
        ...                                            ignore_const_cols=False,
        ...                                            seed=1234)
        >>> iris_glrm.train(x=iris.names, training_frame=iris)
        >>> iris_glrm.show()
        """
        return self._parms.get("ignore_const_cols")

    @ignore_const_cols.setter
    def ignore_const_cols(self, ignore_const_cols):
        assert_is_type(ignore_const_cols, None, bool)
        self._parms["ignore_const_cols"] = ignore_const_cols


    @property
    def score_each_iteration(self):
        """
        Whether to score during each iteration of model training.

        Type: ``bool``  (default: ``False``).

        :examples:

        >>> prostate = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/prostate/prostate_cat.csv")
        >>> prostate[0] = prostate[0].asnumeric()
        >>> prostate[4] = prostate[4].asnumeric()
        >>> loss_all = ["Hinge", "Quadratic", "Categorical", "Categorical",
        ...             "Hinge", "Quadratic", "Quadratic", "Quadratic"]
        >>> pros_glrm = H2OGeneralizedLowRankEstimator(k=5,
        ...                                            loss_by_col=loss_all,
        ...                                            score_each_iteration=True,
        ...                                            transform="standardize",
        ...                                            seed=12345)
        >>> pros_glrm.train(x=prostate.names, training_frame=prostate)
        >>> pros_glrm.show()
        """
        return self._parms.get("score_each_iteration")

    @score_each_iteration.setter
    def score_each_iteration(self, score_each_iteration):
        assert_is_type(score_each_iteration, None, bool)
        self._parms["score_each_iteration"] = score_each_iteration


    @property
    def loading_name(self):
        """
        Frame key to save resulting X

        Type: ``str``.

        :examples:

        >>> acs = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/bigdata/laptop/census/ACS_13_5YR_DP02_cleaned.zip")
        >>> acs_fill = acs.drop("ZCTA5")
        >>> acs_glrm = H2OGeneralizedLowRankEstimator(k=10,
        ...                                           transform="standardize",
        ...                                           loss="quadratic",
        ...                                           regularization_x="quadratic",
        ...                                           regularization_y="L1",
        ...                                           gamma_x=0.25,
        ...                                           gamma_y=0.5,
        ...                                           max_iterations=1,
        ...                                           loading_name="acs_full")
        >>> acs_glrm.train(x=acs_fill.names, training_frame=acs)
        >>> acs_glrm.loading_name
        >>> acs_glrm.show()
        """
        return self._parms.get("loading_name")

    @loading_name.setter
    def loading_name(self, loading_name):
        assert_is_type(loading_name, None, str)
        self._parms["loading_name"] = loading_name


    @property
    def transform(self):
        """
        Transformation of training data

        One of: ``"none"``, ``"standardize"``, ``"normalize"``, ``"demean"``, ``"descale"``  (default: ``"none"``).

        :examples:

        >>> prostate = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/prostate/prostate_cat.csv")
        >>> prostate[0] = prostate[0].asnumeric()
        >>> prostate[4] = prostate[4].asnumeric()
        >>> pros_glrm = H2OGeneralizedLowRankEstimator(k=5,
        ...                                            score_each_iteration=True,
        ...                                            transform="standardize",
        ...                                            seed=12345)
        >>> pros_glrm.train(x=prostate.names, training_frame=prostate)
        >>> pros_glrm.show()
        """
        return self._parms.get("transform")

    @transform.setter
    def transform(self, transform):
        assert_is_type(transform, None, Enum("none", "standardize", "normalize", "demean", "descale"))
        self._parms["transform"] = transform


    @property
    def k(self):
        """
        Rank of matrix approximation

        Type: ``int``  (default: ``1``).

        :examples:

        >>> iris = h2o.import_file("http://h2o-public-test-data.s3.amazonaws.com/smalldata/iris/iris_wheader.csv")
        >>> iris_glrm = H2OGeneralizedLowRankEstimator(k=3)
        >>> iris_glrm.train(x=iris.names, training_frame=iris)
        >>> iris_glrm.show()
        """
        return self._parms.get("k")

    @k.setter
    def k(self, k):
        assert_is_type(k, None, int)
        self._parms["k"] = k


    @property
    def loss(self):
        """
        Numeric loss function

        One of: ``"quadratic"``, ``"absolute"``, ``"huber"``, ``"poisson"``, ``"hinge"``, ``"logistic"``, ``"periodic"``
        (default: ``"quadratic"``).

        :examples:

        >>> acs = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/bigdata/laptop/census/ACS_13_5YR_DP02_cleaned.zip")
        >>> acs_fill = acs.drop("ZCTA5")
        >>> acs_glrm = H2OGeneralizedLowRankEstimator(k=10,
        ...                                           transform="standardize",
        ...                                           loss="absolute",
        ...                                           regularization_x="quadratic",
        ...                                           regularization_y="L1",
        ...                                           gamma_x=0.25,
        ...                                           gamma_y=0.5,
        ...                                           max_iterations=700)
        >>> acs_glrm.train(x=acs_fill.names, training_frame=acs)
        >>> acs_glrm.show()
        """
        return self._parms.get("loss")

    @loss.setter
    def loss(self, loss):
        assert_is_type(loss, None, Enum("quadratic", "absolute", "huber", "poisson", "hinge", "logistic", "periodic"))
        self._parms["loss"] = loss


    @property
    def loss_by_col(self):
        """
        Loss function by column (override)

        Type: ``List[Enum["quadratic", "absolute", "huber", "poisson", "hinge", "logistic", "periodic", "categorical",
        "ordinal"]]``.

        :examples:

        >>> arrestsH2O = h2o.import_file("http://h2o-public-test-data.s3.amazonaws.com/smalldata/pca_test/USArrests.csv")
        >>> arrests_glrm = H2OGeneralizedLowRankEstimator(k=3,
        ...                                               loss="quadratic",
        ...                                               loss_by_col=["absolute","huber"],
        ...                                               loss_by_col_idx=[0,3],
        ...                                               regularization_x="quadratic",
        ...                                               regularization_y="l1")
        >>> arrests_glrm.train(x=arrestsH2O.names, training_frame=arrestsH2O)
        >>> arrests_glrm.show()
        """
        return self._parms.get("loss_by_col")

    @loss_by_col.setter
    def loss_by_col(self, loss_by_col):
        assert_is_type(loss_by_col, None, [Enum("quadratic", "absolute", "huber", "poisson", "hinge", "logistic", "periodic", "categorical", "ordinal")])
        self._parms["loss_by_col"] = loss_by_col


    @property
    def loss_by_col_idx(self):
        """
        Loss function by column index (override)

        Type: ``List[int]``.

        :examples:

        >>> arrestsH2O = h2o.import_file("http://h2o-public-test-data.s3.amazonaws.com/smalldata/pca_test/USArrests.csv")
        >>> arrests_glrm = H2OGeneralizedLowRankEstimator(k=3,
        ...                                               loss="quadratic",
        ...                                               loss_by_col=["absolute","huber"],
        ...                                               loss_by_col_idx=[0,3],
        ...                                               regularization_x="quadratic",
        ...                                               regularization_y="l1")
        >>> arrests_glrm.train(x=arrestsH2O.names, training_frame=arrestsH2O)
        >>> arrests_glrm.show()
        """
        return self._parms.get("loss_by_col_idx")

    @loss_by_col_idx.setter
    def loss_by_col_idx(self, loss_by_col_idx):
        assert_is_type(loss_by_col_idx, None, [int])
        self._parms["loss_by_col_idx"] = loss_by_col_idx


    @property
    def multi_loss(self):
        """
        Categorical loss function

        One of: ``"categorical"``, ``"ordinal"``  (default: ``"categorical"``).

        :examples:

        >>> arrestsH2O = h2o.import_file("http://h2o-public-test-data.s3.amazonaws.com/smalldata/pca_test/USArrests.csv")
        >>> arrests_glrm = H2OGeneralizedLowRankEstimator(k=3,
        ...                                               loss="quadratic",
        ...                                               loss_by_col=["absolute","huber"],
        ...                                               loss_by_col_idx=[0,3],
        ...                                               regularization_x="quadratic",
        ...                                               regularization_y="l1"
        ...                                               multi_loss="ordinal")
        >>> arrests_glrm.train(x=arrestsH2O.names, training_frame=arrestsH2O)
        >>> arrests_glrm.show()
        """
        return self._parms.get("multi_loss")

    @multi_loss.setter
    def multi_loss(self, multi_loss):
        assert_is_type(multi_loss, None, Enum("categorical", "ordinal"))
        self._parms["multi_loss"] = multi_loss


    @property
    def period(self):
        """
        Length of period (only used with periodic loss function)

        Type: ``int``  (default: ``1``).

        :examples:

        >>> arrestsH2O = h2o.import_file("http://h2o-public-test-data.s3.amazonaws.com/smalldata/pca_test/USArrests.csv")
        >>> arrests_glrm = H2OGeneralizedLowRankEstimator(k=3,
        ...                                               max_runtime_secs=15,
        ...                                               max_iterations=500,
        ...                                               max_updates=900,
        ...                                               min_step_size=0.005,
        ...                                               period=5)
        >>> arrests_glrm.train(x=arrestsH2O.names, training_frame=arrestsH2O)
        >>> arrests_glrm.show()
        """
        return self._parms.get("period")

    @period.setter
    def period(self, period):
        assert_is_type(period, None, int)
        self._parms["period"] = period


    @property
    def regularization_x(self):
        """
        Regularization function for X matrix

        One of: ``"none"``, ``"quadratic"``, ``"l2"``, ``"l1"``, ``"non_negative"``, ``"one_sparse"``,
        ``"unit_one_sparse"``, ``"simplex"``  (default: ``"none"``).

        :examples:

        >>> arrestsH2O = h2o.import_file("http://h2o-public-test-data.s3.amazonaws.com/smalldata/pca_test/USArrests.csv")
        >>> arrests_glrm = H2OGeneralizedLowRankEstimator(k=3,
        ...                                               loss="quadratic",
        ...                                               loss_by_col=["absolute","huber"],
        ...                                               loss_by_col_idx=[0,3],
        ...                                               regularization_x="quadratic",
        ...                                               regularization_y="l1")
        >>> arrests_glrm.train(x=arrestsH2O.names, training_frame=arrestsH2O)
        >>> arrests_glrm.show()
        """
        return self._parms.get("regularization_x")

    @regularization_x.setter
    def regularization_x(self, regularization_x):
        assert_is_type(regularization_x, None, Enum("none", "quadratic", "l2", "l1", "non_negative", "one_sparse", "unit_one_sparse", "simplex"))
        self._parms["regularization_x"] = regularization_x


    @property
    def regularization_y(self):
        """
        Regularization function for Y matrix

        One of: ``"none"``, ``"quadratic"``, ``"l2"``, ``"l1"``, ``"non_negative"``, ``"one_sparse"``,
        ``"unit_one_sparse"``, ``"simplex"``  (default: ``"none"``).

        :examples:

        >>> arrestsH2O = h2o.import_file("http://h2o-public-test-data.s3.amazonaws.com/smalldata/pca_test/USArrests.csv")
        >>> arrests_glrm = H2OGeneralizedLowRankEstimator(k=3,
        ...                                               loss="quadratic",
        ...                                               loss_by_col=["absolute","huber"],
        ...                                               loss_by_col_idx=[0,3],
        ...                                               regularization_x="quadratic",
        ...                                               regularization_y="l1")
        >>> arrests_glrm.train(x=arrestsH2O.names, training_frame=arrestsH2O)
        >>> arrests_glrm.show()
        """
        return self._parms.get("regularization_y")

    @regularization_y.setter
    def regularization_y(self, regularization_y):
        assert_is_type(regularization_y, None, Enum("none", "quadratic", "l2", "l1", "non_negative", "one_sparse", "unit_one_sparse", "simplex"))
        self._parms["regularization_y"] = regularization_y


    @property
    def gamma_x(self):
        """
        Regularization weight on X matrix

        Type: ``float``  (default: ``0``).

        :examples:

        >>> iris = h2o.import_file("http://h2o-public-test-data.s3.amazonaws.com/smalldata/iris/iris_wheader.csv")
        >>> rank = 3
        >>> gx = 0.5
        >>> gy = 0.5
        >>> trans = "standardize"
        >>> iris_glrm = H2OGeneralizedLowRankEstimator(k=rank,
        ...                                            loss="Quadratic",
        ...                                            gamma_x=gx,
        ...                                            gamma_y=gy,
        ...                                            transform=trans)
        >>> iris_glrm.train(x=iris.names, training_frame=iris)
        >>> iris_glrm.show()
        """
        return self._parms.get("gamma_x")

    @gamma_x.setter
    def gamma_x(self, gamma_x):
        assert_is_type(gamma_x, None, numeric)
        self._parms["gamma_x"] = gamma_x


    @property
    def gamma_y(self):
        """
        Regularization weight on Y matrix

        Type: ``float``  (default: ``0``).

        :examples:

        >>> iris = h2o.import_file("http://h2o-public-test-data.s3.amazonaws.com/smalldata/iris/iris_wheader.csv")
        >>> rank = 3
        >>> gx = 0.5
        >>> gy = 0.5
        >>> trans = "standardize"
        >>> iris_glrm = H2OGeneralizedLowRankEstimator(k=rank,
        ...                                            loss="Quadratic",
        ...                                            gamma_x=gx,
        ...                                            gamma_y=gy,
        ...                                            transform=trans)
        >>> iris_glrm.train(x=iris.names, training_frame=iris)
        >>> iris_glrm.show()
        """
        return self._parms.get("gamma_y")

    @gamma_y.setter
    def gamma_y(self, gamma_y):
        assert_is_type(gamma_y, None, numeric)
        self._parms["gamma_y"] = gamma_y


    @property
    def max_iterations(self):
        """
        Maximum number of iterations

        Type: ``int``  (default: ``1000``).

        :examples:

        >>> acs = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/bigdata/laptop/census/ACS_13_5YR_DP02_cleaned.zip")
        >>> acs_fill = acs.drop("ZCTA5")
        >>> acs_glrm = H2OGeneralizedLowRankEstimator(k=10,
        ...                                           transform="standardize",
        ...                                           loss="quadratic",
        ...                                           regularization_x="quadratic",
        ...                                           regularization_y="L1",
        ...                                           gamma_x=0.25,
        ...                                           gamma_y=0.5,
        ...                                           max_iterations=700)
        >>> acs_glrm.train(x=acs_fill.names, training_frame=acs)
        >>> acs_glrm.show()
        """
        return self._parms.get("max_iterations")

    @max_iterations.setter
    def max_iterations(self, max_iterations):
        assert_is_type(max_iterations, None, int)
        self._parms["max_iterations"] = max_iterations


    @property
    def max_updates(self):
        """
        Maximum number of updates, defaults to 2*max_iterations

        Type: ``int``  (default: ``2000``).

        :examples:

        >>> arrestsH2O = h2o.import_file("http://h2o-public-test-data.s3.amazonaws.com/smalldata/pca_test/USArrests.csv")
        >>> arrests_glrm = H2OGeneralizedLowRankEstimator(k=3,
        ...                                               max_runtime_secs=15,
        ...                                               max_iterations=500,
        ...                                               max_updates=900,
        ...                                               min_step_size=0.005)
        >>> arrests_glrm.train(x=arrestsH2O.names, training_frame=arrestsH2O)
        >>> arrests_glrm.show()
        """
        return self._parms.get("max_updates")

    @max_updates.setter
    def max_updates(self, max_updates):
        assert_is_type(max_updates, None, int)
        self._parms["max_updates"] = max_updates


    @property
    def init_step_size(self):
        """
        Initial step size

        Type: ``float``  (default: ``1``).

        :examples:

        >>> iris = h2o.import_file("http://h2o-public-test-data.s3.amazonaws.com/smalldata/iris/iris_wheader.csv")
        >>> iris_glrm = H2OGeneralizedLowRankEstimator(k=3,
        ...                                            init_step_size=2.5,
        ...                                            seed=1234) 
        >>> iris_glrm.train(x=iris.names, training_frame=iris)
        >>> iris_glrm.show()
        """
        return self._parms.get("init_step_size")

    @init_step_size.setter
    def init_step_size(self, init_step_size):
        assert_is_type(init_step_size, None, numeric)
        self._parms["init_step_size"] = init_step_size


    @property
    def min_step_size(self):
        """
        Minimum step size

        Type: ``float``  (default: ``0.0001``).

        :examples:

        >>> arrestsH2O = h2o.import_file("http://h2o-public-test-data.s3.amazonaws.com/smalldata/pca_test/USArrests.csv")
        >>> arrests_glrm = H2OGeneralizedLowRankEstimator(k=3,
        ...                                               max_runtime_secs=15,
        ...                                               max_iterations=500,
        ...                                               max_updates=900,
        ...                                               min_step_size=0.005)
        >>> arrests_glrm.train(x=arrestsH2O.names, training_frame=arrestsH2O)
        >>> arrests_glrm.show()
        """
        return self._parms.get("min_step_size")

    @min_step_size.setter
    def min_step_size(self, min_step_size):
        assert_is_type(min_step_size, None, numeric)
        self._parms["min_step_size"] = min_step_size


    @property
    def seed(self):
        """
        RNG seed for initialization

        Type: ``int``  (default: ``-1``).

        :examples:

        >>> prostate = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/prostate/prostate_cat.csv")
        >>> prostate[0] = prostate[0].asnumeric()
        >>> prostate[4] = prostate[4].asnumeric()
        >>> glrm_w_seed = H2OGeneralizedLowRankEstimator(k=5, seed=12345) 
        >>> glrm_w_seed.train(x=prostate.names, training_frame=prostate)
        >>> glrm_wo_seed = H2OGeneralizedLowRankEstimator(k=5, 
        >>> glrm_wo_seed.train(x=prostate.names, training_frame=prostate)
        >>> glrm_w_seed.show()
        >>> glrm_wo_seed.show()
        """
        return self._parms.get("seed")

    @seed.setter
    def seed(self, seed):
        assert_is_type(seed, None, int)
        self._parms["seed"] = seed


    @property
    def init(self):
        """
        Initialization mode

        One of: ``"random"``, ``"svd"``, ``"plus_plus"``, ``"user"``  (default: ``"plus_plus"``).

        :examples:

        >>> iris = h2o.import_file("http://h2o-public-test-data.s3.amazonaws.com/smalldata/iris/iris_wheader.csv")
        >>> iris_glrm = H2OGeneralizedLowRankEstimator(k=3,
        ...                                            init="svd",
        ...                                            seed=1234) 
        >>> iris_glrm.train(x=iris.names, training_frame=iris)
        >>> iris_glrm.show()
        """
        return self._parms.get("init")

    @init.setter
    def init(self, init):
        assert_is_type(init, None, Enum("random", "svd", "plus_plus", "user"))
        self._parms["init"] = init


    @property
    def svd_method(self):
        """
        Method for computing SVD during initialization (Caution: Randomized is currently experimental and unstable)

        One of: ``"gram_s_v_d"``, ``"power"``, ``"randomized"``  (default: ``"randomized"``).

        :examples:

        >>> prostate = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/prostate/prostate_cat.csv")
        >>> prostate[0] = prostate[0].asnumeric()
        >>> prostate[4] = prostate[4].asnumeric()
        >>> pros_glrm = H2OGeneralizedLowRankEstimator(k=5,
        ...                                            svd_method="power",
        ...                                            seed=1234)
        >>> pros_glrm.train(x=prostate.names, training_frame=prostate)
        >>> pros_glrm.show()
        """
        return self._parms.get("svd_method")

    @svd_method.setter
    def svd_method(self, svd_method):
        assert_is_type(svd_method, None, Enum("gram_s_v_d", "power", "randomized"))
        self._parms["svd_method"] = svd_method


    @property
    def user_y(self):
        """
        User-specified initial Y

        Type: ``H2OFrame``.

        :examples:

        >>> arrestsH2O = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/pca_test/USArrests.csv")
        >>> initial_y = [[5.412,  65.24,  -7.54, -0.032],
        ...              [2.212,  92.24, -17.54, 23.268],
        ...              [0.312, 123.24,  14.46,  9.768],
        ...              [1.012,  19.24, -15.54, -1.732]]
        >>> initial_y_h2o = h2o.H2OFrame(list(zip(*initial_y)))
        >>> arrests_glrm = H2OGeneralizedLowRankEstimator(k=4,
        ...                                               transform="demean",
        ...                                               loss="quadratic",
        ...                                               gamma_x=0.5,
        ...                                               gamma_y=0.3,
        ...                                               init="user",
        ...                                               user_y=initial_y_h2o,
        ...                                               recover_svd=True)
        >>> arrests_glrm.train(x=arrestsH2O.names, training_frame=arrestsH2O)
        >>> arrests_glrm.show()
        """
        return self._parms.get("user_y")

    @user_y.setter
    def user_y(self, user_y):
        self._parms["user_y"] = H2OFrame._validate(user_y, 'user_y')


    @property
    def user_x(self):
        """
        User-specified initial X

        Type: ``H2OFrame``.

        :examples:

        >>> arrestsH2O = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/pca_test/USArrests.csv")
        >>> initial_x = ([[5.412, 65.24, -7.54, -0.032, 2.212, 92.24, -17.54, 23.268, 0.312,
        ...                123.24, 14.46, 9.768, 1.012, 19.24, -15.54, -1.732, 5.412, 65.24,
        ...                -7.54, -0.032, 2.212, 92.24, -17.54, 23.268, 0.312, 123.24, 14.46,
        ...                9.76, 1.012, 19.24, -15.54, -1.732, 5.412, 65.24, -7.54, -0.032,
        ...                2.212, 92.24, -17.54, 23.268, 0.312, 123.24, 14.46, 9.768, 1.012,
        ...                19.24, -15.54, -1.732, 5.412, 65.24]]*4)
        >>> initial_x_h2o = h2o.H2OFrame(list(zip(*initial_x)))
        >>> arrests_glrm = H2OGeneralizedLowRankEstimator(k=4,
        ...                                               transform="demean",
        ...                                               loss="quadratic",
        ...                                               gamma_x=0.5,
        ...                                               gamma_y=0.3,
        ...                                               init="user",
        ...                                               user_x=initial_x_h2o,
        ...                                               recover_svd=True)
        >>> arrests_glrm.train(x=arrestsH2O.names, training_frame=arrestsH2O)
        >>> arrests_glrm.show()
        """
        return self._parms.get("user_x")

    @user_x.setter
    def user_x(self, user_x):
        self._parms["user_x"] = H2OFrame._validate(user_x, 'user_x')


    @property
    def expand_user_y(self):
        """
        Expand categorical columns in user-specified initial Y

        Type: ``bool``  (default: ``True``).

        :examples:

        >>> iris = h2o.import_file("http://h2o-public-test-data.s3.amazonaws.com/smalldata/iris/iris_wheader.csv")
        >>> rank = 3
        >>> gx = 0.5
        >>> gy = 0.5
        >>> trans = "standardize"
        >>> iris_glrm = H2OGeneralizedLowRankEstimator(k=rank,
        ...                                            loss="Quadratic",
        ...                                            gamma_x=gx,
        ...                                            gamma_y=gy,
        ...                                            transform=trans,
        ...                                            expand_user_y=False)
        >>> iris_glrm.train(x=iris.names, training_frame=iris)
        >>> iris_glrm.show()
        """
        return self._parms.get("expand_user_y")

    @expand_user_y.setter
    def expand_user_y(self, expand_user_y):
        assert_is_type(expand_user_y, None, bool)
        self._parms["expand_user_y"] = expand_user_y


    @property
    def impute_original(self):
        """
        Reconstruct original training data by reversing transform

        Type: ``bool``  (default: ``False``).

        :examples:

        >>> iris = h2o.import_file("http://h2o-public-test-data.s3.amazonaws.com/smalldata/iris/iris_wheader.csv")
        >>> rank = 3
        >>> gx = 0.5
        >>> gy = 0.5
        >>> trans = "standardize"
        >>> iris_glrm = H2OGeneralizedLowRankEstimator(k=rank,
        ...                                            loss="Quadratic",
        ...                                            gamma_x=gx,
        ...                                            gamma_y=gy,
        ...                                            transform=trans
        ...                                            impute_original=True)
        >>> iris_glrm.train(x=iris.names, training_frame=iris)
        >>> iris_glrm.show()
        """
        return self._parms.get("impute_original")

    @impute_original.setter
    def impute_original(self, impute_original):
        assert_is_type(impute_original, None, bool)
        self._parms["impute_original"] = impute_original


    @property
    def recover_svd(self):
        """
        Recover singular values and eigenvectors of XY

        Type: ``bool``  (default: ``False``).

        :examples:

        >>> prostate = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/prostate/prostate_cat.csv")
        >>> prostate[0] = prostate[0].asnumeric()
        >>> prostate[4] = prostate[4].asnumeric()
        >>> loss_all = ["Hinge", "Quadratic", "Categorical", "Categorical",
        ...             "Hinge", "Quadratic", "Quadratic", "Quadratic"]
        >>> pros_glrm = H2OGeneralizedLowRankEstimator(k=5,
        ...                                            loss_by_col=loss_all,
        ...                                            recover_svd=True,
        ...                                            transform="standardize",
        ...                                            seed=12345)
        >>> pros_glrm.train(x=prostate.names, training_frame=prostate)
        >>> pros_glrm.show()
        """
        return self._parms.get("recover_svd")

    @recover_svd.setter
    def recover_svd(self, recover_svd):
        assert_is_type(recover_svd, None, bool)
        self._parms["recover_svd"] = recover_svd


    @property
    def max_runtime_secs(self):
        """
        Maximum allowed runtime in seconds for model training. Use 0 to disable.

        Type: ``float``  (default: ``0``).

        :examples:

        >>> arrestsH2O = h2o.import_file("http://h2o-public-test-data.s3.amazonaws.com/smalldata/pca_test/USArrests.csv")
        >>> arrests_glrm = H2OGeneralizedLowRankEstimator(k=3,
        ...                                               max_runtime_secs=15,
        ...                                               max_iterations=500,
        ...                                               max_updates=900,
        ...                                               min_step_size=0.005)
        >>> arrests_glrm.train(x=arrestsH2O.names, training_frame=arrestsH2O)
        >>> arrests_glrm.show()
        """
        return self._parms.get("max_runtime_secs")

    @max_runtime_secs.setter
    def max_runtime_secs(self, max_runtime_secs):
        assert_is_type(max_runtime_secs, None, numeric)
        self._parms["max_runtime_secs"] = max_runtime_secs


    @property
    def export_checkpoints_dir(self):
        """
        Automatically export generated models to this directory.

        Type: ``str``.

        :examples:

        >>> import tempfile
        >>> from os import listdir
        >>> iris = h2o.import_file("http://h2o-public-test-data.s3.amazonaws.com/smalldata/iris/iris_wheader.csv")
        >>> checkpoints_dir = tempfile.mkdtemp()
        >>> iris_glrm = H2OGeneralizedLowRankEstimator(k=3,
        ...                                            export_checkpoints_dir=checkpoints_dir,
        ...                                            seed=1234)
        >>> iris_glrm.train(x=iris.names, training_frame=iris)
        >>> len(listdir(checkpoints_dir))
        """
        return self._parms.get("export_checkpoints_dir")

    @export_checkpoints_dir.setter
    def export_checkpoints_dir(self, export_checkpoints_dir):
        assert_is_type(export_checkpoints_dir, None, str)
        self._parms["export_checkpoints_dir"] = export_checkpoints_dir


