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
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Set the file path
filepath = 'data/m-gm3dx7508.txt.gz'
# Load the data
df = pd.read_csv(filepath, delimiter='\s+', parse_dates=['date'])
# Without Time Series in Column 2 contains GM stock returns
gm = df['gm']
# Set the Time Series
gm1 = df.set_index('date')
# Column 2 contains GM stock returns
gm1 = gm1['gm']

# Put four plots on a page
plt.figure()

ax1 = plt.subplot2grid((4, 1), (0, 0))
gm.plot(ax=ax1)
ax2 = plt.subplot2grid((4, 1), (1, 0))
gm1.plot(ax=ax2)

ax3 = plt.subplot2grid((4, 1), (2, 0))
sm.graphics.tsa.plot_acf(gm, lags=24, ax=ax3)
ax4 = plt.subplot2grid((4, 1), (3, 0))
sm.graphics.tsa.plot_acf(gm1, lags=24, ax=ax4)

plt.show()
