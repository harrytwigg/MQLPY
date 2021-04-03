"""Copy ticks from Metatrader5 and store them in the database"""

from datetime import datetime, tzinfo
from logging import debug, error
from os import read
from arctic import Arctic
from arctic.arctic import TICK_STORE
from dateutil.relativedelta import relativedelta
import pytz
import MetaTrader5 as mt5
import pandas as pd


def import_data(symbol, from_date, to_date, requested_library, requested_store='192.168.0.43'):
    """Standardised function to import data and save it in the database, make sure UTC dateTimes are specified"""

    if not mt5.initialize():
        error("initialize() failed, error code =", mt5.last_error())
        quit()

    # Connect to Local MONGODB
    store = Arctic(requested_store)

    store.initialize_library(requested_library)

    # Access the library
    library = store[requested_library]

    current_date = from_date
    while current_date <= to_date:
        daily_ticks = mt5.copy_ticks_range(
            symbol, current_date, current_date + relativedelta(days=1), mt5.COPY_TICKS_ALL)
        daily_ticks_df = pd.DataFrame(daily_ticks)
        daily_ticks_df['time'] = pd.to_datetime(
            daily_ticks_df['time'], unit='s')

        # Store the data in the library
        current_date_string = current_date.strftime("%d/%m/%Y")
        library.write(current_date_string, daily_ticks_df)

        print(len(daily_ticks), "ticks for symbol", symbol,
              "date", current_date_string, "were added to the library", requested_library, "on the store", requested_store)

        current_date += relativedelta(days=1)

    # shut down connection to the MetaTrader 5 terminal
    mt5.shutdown()


def read_data(requested_symbol, requested_library='Pepperstone MT5 Razor', requested_store='192.168.0.43'):
    store = Arctic(requested_store)
    library = store[requested_library]
    extractedData = library.read(requested_symbol)
    return extractedData.data


timezone = pytz.timezone("ETC/UTC")
from_date = datetime(2019, 2, 4, tzinfo=timezone)
to_date = datetime(2021, 4, 3, tzinfo=timezone)
store = Arctic("192.168.0.43")
print(store.list_libraries())
#store.delete_library('Pepperstone MT5 Razor')
#import_data('GBPUSD', from_date, to_date,
#            requested_library='Pep MT5 GBPUSD Tick Data')
print(read_data('EURUSD 1M', requested_library="FX OHLCs").head(10))