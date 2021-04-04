"""The backtester program manager"""

from datetime import datetime
from arctic import Arctic
from dateutil.relativedelta import relativedelta
from mqlpy.constants_enumerations_structures.data_source_constants import *
from mqlpy.constants_enumerations_structures.trade_constants import Timeframes
import pandas as pd
import logging


class BacktestProgramManager:
    """A program manager that takes an expert and a backtest compatible order manager, then performs a single backtest on the EA"""

    def __init__(self, order_manager, expert, start_time, data_interval, end_time=datetime.utcnow()):
        self.data_buffer = []
        data_buffer_names = []
        data_buffer_current_positions = []
        self.start_time = start_time
        self.end_time = end_time

        if data_interval == Timeframes.PERIOD_M1:
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
                                logging.error(
                                    DataOp.STRINGED_LIBRARY, "has not been implemented yet")
                                break

                            self.data_buffer.append(
                                self.arctic_libraries[incrementor_2].read(l).data)
                            data_buffer_names.append(l)
                            data_buffer_current_positions.append(0)

                        incrementor_2 += 1
                    incrementor += 1

        # Trim data outside of the entire test dataset
        for buffer_index in range(0, len(self.data_buffer)):
            self.data_buffer[buffer_index] = self.data_buffer[buffer_index].sort_index(
            ).truncate(before=self.start_time, after=self.end_time)

        current_time = self.start_time
        current_index
        while current_time <= end_time:
            data_selection = 
            expert.on_data(order_manager, self.data_buffer_selection(self.data_buffer, self.start_time, current_time), current_time)
            current_time += relative_delta

    # Trm data buffer maybe rewrtite for performance
    def data_buffer_selection(self, buffers_object, start_time, current_time):
        """Returns a trimmed data buffer for the current time"""
        return [buffers_object[buffer_index].truncate(before=start_time, after=current_time) for buffer_index in range(0, len(buffers_object))]
