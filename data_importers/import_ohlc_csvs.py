"""Imports OHLC data from CSVs
https://www.histdata.com"""

import glob
import pandas as pd
from arctic import Arctic
from arctic.arctic import TICK_STORE


path = r"C:\Users\harry\Documents\Downloaded Symbol Data\FX OHLC 1M\GBPUSD\*.csv"

merged = pd.DataFrame(columns=["time","open", "high", "low", "close"])

for fname in glob.glob(path):
    df=pd.read_csv(fname, sep=';', names=["time","open", "high", "low", "close", "?"])
    df['time'] = pd.to_datetime(df['time'], format='%Y%m%d %H%M%S')
    merged=merged.append(df.drop(columns="?"))

# Optionally set the timestamp as the index
merged = merged.set_index("time")

print(merged.head(10))


# Now time to add to the database

store = Arctic('192.168.0.43')
store.initialize_library('FX OHLC 1M')
library = store['FX OHLC 1M']
library.write('GBPUSD', merged)