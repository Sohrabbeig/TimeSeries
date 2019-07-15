# %%
# plot the whole serie
import pandas as pd
import matplotlib.pyplot as plt

dt = pd.read_csv("data/diet.csv", squeeze=True, index_col='Month')
dt.index = pd.to_datetime(dt.index)
dt.plot(grid=True)
plt.ylabel("diet")
plt.show()

# %%
# plot only datas from 2012 year

dt2012 = dt['2012']
dt2012.plot(grid=True)
plt.show()

# %%
# working with join
df = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],
                   'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']})

other = pd.DataFrame({'key': ['K0', 'K1', 'K2'], 'B': ['B0', 'B1', 'B2']})
j = df.set_index('key').join(other.set_index('key'),  how='inner')
