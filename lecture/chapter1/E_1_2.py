from math import sqrt
import pandas as pd
import numpy as np
import scipy.stats as stats

# Set the file path
filepath = 'data/d-ibm3dx7008.txt.gz'
# Load the data
ibm = pd.read_csv(filepath, delimiter='\s+').iloc[:, 1]
# Percentage simple returns
sibm = ibm * 100

# compute the summary statistics
summary = sibm.describe()
print(summary)

# Alternatively, one can use individual commands as follows:
# 算术平均值
mean = sibm.mean()
print(f'mean={mean:.8f}')
# 中位数
median = sibm.median()
print(f'median={median:.8f}')
# 方差
var = sibm.var()
print(f'var={var:.8f}')
# 标准差
std = sibm.std()
print('std(sqrt)={std:.8f}')
# 偏度
skewness = sibm.skew()
print(f'skewness={skewness:.8f}')
# 峰度
kurtosis = sibm.kurt()
print(f'kurtosis={kurtosis:.8f}')

# Simple tests
s1 = sibm.skew()
# Compute test statistic
t1 = s1 / sqrt(6.0 / len(sibm))
print(f't1={t1:.8f}')

# Compute p-value
pv = 2 * (1 - stats.norm.cdf(t1))
print(f'pv={pv:.8f}')

# Turn to log returns in percentages
libm = np.log(ibm + 1) * 100
libm = libm.values
# Test mean being zero,One sample t-test
t, p_value = stats.ttest_1samp(libm, 0)
print('One sample t-test:')
print(f't={t:.4f}, p-value={p_value:.4f}\n')
# The result shows that the hypothesis of zero expected return
# cannot be rejected as the 5% or 10% level

# Normality test
statistic_x_squared, p_value = stats.jarque_bera(libm)
print('Normality test:')
print(f'STATISTIC:X-squared={statistic_x_squared:.4f},P-VALUE:Asymptotic_p_Value={p_value}\n')
# The result shows the normality for log-return is rejuected
