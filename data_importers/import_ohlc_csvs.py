"""Imports OHLC data from CSVs
https://www.histdata.com"""

import glob
import pandas as pd
from datetime import datetime
from arctic import Arctic
from arctic.arctic import TICK_STORE


path = r"C:\Users\harry\Downloads\Downloaded Data\*.csv"

merged = pd.DataFrame(columns=["time","open", "high", "low", "close"])

for fname in glob.glob(path):
    df=pd.read_csv(fname, sep=';', names=["time","open", "high", "low", "close", "?"])
    df['time'] = pd.to_datetime(df['time'], format='%Y%m%d %H%M%S')
    merged=merged.append(df.drop(columns="?"))

merged = merged.set_index("time")

print(merged.head(10))


# Now time to add to the database

store = Arctic('192.168.0.43')
store.initialize_library('FX OHLCs')
library = store['FX OHLCs']
library.write('EURUSD 1M', merged)