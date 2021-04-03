"""Data source constants to use throughout the program"""

from enum import Enum

class DataSource(Enum):
    """Enums for different sources of data"""
    ARCTIC_SOURCE = 0

class DataOp(Enum):
    """Specify an advance selection of timeseries data from a library"""
    STRINGED_LIBRARY = "stringed library"