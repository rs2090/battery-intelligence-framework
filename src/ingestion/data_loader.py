"""
Data loader for battery datasets.
"""
import pandas as pd
import numpy as np


def load_battery_data(file_path):
    """
    Load battery data from a CSV or other structured file.
    :param file_path: Path to the data file.
    :return: pandas.DataFrame containing the loaded data.
    """
    return pd.read_csv(file_path)
