"""The backtester program manager"""

from datetime import datetime
from arctic import Arctic
from mqlpy.constants_enumerations_structures.data_source_constants import *
import pandas as pd
import logging
import time


class BacktestProgramManager:
    """A program manager that takes an expert and a backtest compatible order manager, then performs a single backtest on the EA"""

    def __init__(self, order_manager, expert, start_time, data_interval, end_time=datetime.utcnow()):
        self.data_buffer = pd.DataFrame()  # Data buffer that can be reused between tests

        for i in expert.data_sources:  # i is the datasource

            if i == DataSource.ARCTIC_SOURCE:
                arctic_stores = []
                arctic_libraries = []
                incrementor = 0  # incrementor is interger index of j

                # j is the location of the arctic source
                for j in expert.data_sources[DataSource.ARCTIC_SOURCE]:
                    arctic_stores.append(Arctic(j))

                    incrementor_2 = 0  # incrementor_2 is integer index of k

                    # k is the individual libraries
                    for k in expert.data_sources[DataSource.ARCTIC_SOURCE][j]["libraries"]:
                        arctic_libraries.append(
                            arctic_stores[incrementor][k])

                        # l is the symbol in the library
                        # TODO handle special cases
                        for l in expert.data_sources[DataSource.ARCTIC_SOURCE][j]["libraries"][k]:
                            if l == DataOp.STRINGED_LIBRARY:
                                logging.error(
                                    DataOp.STRINGED_LIBRARY, "has not been implemented yet")
                                break
                            else:
                                current_df = arctic_libraries[incrementor_2].read(
                                    l).data
                                columns = current_df.columns.tolist()

                                # Loop through and rename according to the Symbol
                                for i in range(len(columns)):
                                    columns[i] = l + " " + columns[i]
                                current_df.columns = columns

                                # Join current_df to the data_buffer
                                self.data_buffer = self.data_buffer.join(
                                    current_df, how='outer')

                        incrementor_2 += 1
                    incrementor += 1

        # Sort and trim data outside of the entire test dataset
        self.data_buffer = self.data_buffer.sort_index().truncate(
            before=start_time, after=end_time)

        current_index = 1
        start = time.time()

        while current_index <= expert.buffer_size:
            data_selection = self.data_buffer[0:current_index]
            expert.on_data(order_manager, data_selection)
            current_index += 1

        for i in range(expert.buffer_size+1, len(self.data_buffer)):
            data_selection = self.data_buffer[current_index-100:current_index]
            expert.on_data(order_manager, data_selection)
            current_index += 1
        
        end = time.time()
        logging.info("Total simulation time was", end - start, "seconds")
        
