import os
from typing import Tuple, List, Dict

import pandas as pd


def ip_country(db_path: str, ips: Tuple) -> List[Dict]:
    df = get_df(db_path)


def get_df(path_to_csv: str) -> pd.core.frame.DataFrame:
    if not os.path.exists(path_to_csv):
        raise FileNotFoundError(2, 'No such file or directory', path_to_csv)
    df = pd.read_csv(path_to_csv, names=['ip_from', 'ip_to', 'country_code', 'country_name', 'region_name', 'city_name'], index_col=None)
    return df

