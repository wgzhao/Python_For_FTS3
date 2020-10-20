#  Copyright 2020
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import pandas as pd
import numpy as np
import scipy.stats
from statsmodels.api import tsa

def mean_confidence_interval(data: pd.DataFrame, confidence=0.95):
    """
    Compute the confidence interval for specified confidence value

    :param data: list
    :param confidence: percent
    :return: (lower, upper)
    """
    m, se = np.mean(data), data.sem()
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., data.shape[0] - 1)
    return m - h, m + h


def basic_stats(df: pd.DataFrame):
    """
    Compute the summary statistics

    :param df: the pandas's dataframe
    :return: None
    """
    desc = df.describe().to_dict()
    cl_lower, cl_upper = mean_confidence_interval(df, confidence=0.95)
    print(f"""
    {'nobs':<12}{desc['count']:<10} % Sample size 
    {'NAs':<12}{df.isnull().sum():<10} % Number of missing values
    {'Minimum':<12}{desc['min']:<.8f}
    {'Maximum':<12}{desc['max']:<.8f}
    {'1. Quartile':<12}{desc['25%']:<.8f} % 25th percentile
    {'3. Quartile':<12}{desc['75%']:<.8f} % 75th percentile
    {'Mean':<12}{desc['mean']:<.8f} % Sample mean
    {'Median':<12}{df.median():<.8f} % Sample median
    {'Sum':<12}{df.sum():<.8f} % Sum of the percentage simple returns
    {'SE Mean':<12}{df.sem():<.8f} % Standard error of the sample mean(unbias)
    {'LCL Mean':<12}{cl_lower:<.8f} % Lower bound of 95% conf. interval for mean
    {'UCL Mean':<12}{cl_upper:<.8f} % Uppoer bound of 95% conf. interval for mean
    {'Variance':<12}{desc['std']**2:<.8f} % Sample variance
    {'Stdev':<12}{desc['std']:<.8f} % Sample standard error
    {'Skewness':<12}{df.skew():<.8f} % Sample skewness
    {'Kurtosis':<12}{df.kurtosis():<.8f} % Sampke excess kurtosis
    """)


def ljungbox(x:np.ndarray, lags: int =5):
    """
    Compute Ljung-Box

    :param x: numpy 1d array
    :param lags: perioid
    :return: (x-squared, p-value)
    """
    _, _, qstat, pv  = tsa.acf(x, nlags=lags, qstat=True, alpha=0.05, fft=False)
    return qstat[-1], pv[-1]
