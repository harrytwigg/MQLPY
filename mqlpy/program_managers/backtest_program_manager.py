"""The backtester program manager"""

from datetime import datetime
from arctic import Arctic
from dateutil.relativedelta import relativedelta
from mqlpy.constants_enumerations_structures.data_source_constants import *
from mqlpy.constants_enumerations_structures.trade_constants import DataInterval


class BacktestProgramManager:
    """A program manager that takes an expert and a backtest compatible order manager, then performs a single backtest on the EA"""

    def __init__(self, order_manager, expert, start_date, data_interval, end_date=datetime.utcnow()):
        self.data_buffer = []
        self.data_buffer_index = []
        
        data_buffer_current_positions = []

        if data_interval == DataInterval.M1:
            relative_delta = relativedelta(minutes=1)

        for i in expert.data_sources:  # i is the datasource

            if i == DataSource.ARCTIC_SOURCE:
                self.arctic_stores = []
                self.arctic_stores_locations = []
                self.arctic_libraries = []
                self.arctic_library_store_keys = []
                incrementor = 0  # incrementor is interger index of j

                # j is the location of the arctic source
                for j in expert.data_sources[DataSource.ARCTIC_SOURCE]:
                    self.arctic_stores.append(Arctic(j))

                    incrementor_2 = 0  # incrementor_2 is integer index of k

                    # ks are the individual libraries
                    for k in expert.data_sources[DataSource.ARCTIC_SOURCE][j]["libraries"]:
                        self.arctic_libraries.append(
                            self.arctic_stores[incrementor][k])
                        self.arctic_library_store_keys.append(
                            expert.data_sources[DataSource.ARCTIC_SOURCE][j]["libraries"][k])

                        # TODO handle special cases
                        for l in expert.data_sources[DataSource.ARCTIC_SOURCE][j]["libraries"][k]:
                            if l == DataOp.STRINGED_LIBRARY:
                                
                                break

                            self.data_buffer.append(
                                self.arctic_libraries[incrementor_2].read(l).data)
                            self.data_buffer_index.append(l)

                        incrementor_2 += 1

                    incrementor += 1
        
        current_date = start_date
        start_date_formatted = start_date.strftime("%Y-%m-%d %H:%M:%S")
        current_buffer = []
        #current_buffer_indices make pd series then loop through each time and append to the buffer
        while current_date <= end_date:

            for buffer_index in range(0, len(self.data_buffer)):
                print(i.loc[start_date_formatted:current_date.strftime("%Y-%m-%d %H:%M:%S")])
            current_date += relative_delta

