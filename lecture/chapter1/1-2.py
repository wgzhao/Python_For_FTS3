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
"""
计算 IBM 股票收益率的样本偏度和峰度
P9
"""
from math import sqrt
import pandas as pd
import numpy as np
import scipy.stats as stats
from lecture import DATA_DIR
from lecture.utils import basic_stats

# Set the file path
filepath = DATA_DIR.joinpath('d-ibm3dx7008.txt.gz')
# Load the data, the 1st row is column name
ibm = pd.read_csv(filepath, delimiter='\t', header=0)
# print data size, 9845 * 5
print(ibm.shape)
# print the first 3 rows
print(ibm.head(3))
# Percentage simple returns
sibm = ibm.iloc[:, 1] * 100

# compute the summary statistics
basic_stats(sibm)

# Simple tests
s1 = sibm.skew()
# Compute test statistic
t1 = s1 / sqrt(6.0 / len(sibm))
print(f't1={t1:.8f}')

# Compute p-value
pv = 2 * (1 - stats.norm.cdf(t1))
print(f'pv={pv:.8f}')

# Turn to log returns in percentages
libm = np.log(sibm.dropna() / 100.0 + 1) * 100
# Test mean being zero,One sample t-test
t, p_value = stats.ttest_1samp(libm.values, 0.0)

print('One sample t-test:'.center(30,' '))
print("data: libm")
print(f't = {t:<.4f}, df = {libm.shape[0]}, p-value = {p_value:.4f}')
# The result shows that the hypothesis of zero expected return
# cannot be rejected as the 5% or 10% level

# Normality test
statistic_x_squared, p_value = stats.jarque_bera(libm.values)
print('Normality test:')
print(f'STATISTIC:X-squared={statistic_x_squared:.4f},P-VALUE:Asymptotic_p_Value={p_value}\n')
# The result shows the normality for log-return is rejected
