import os
from typing import Dict
import ipaddress

import pandas as pd


class IPCountry:
    def __init__(self, db_path: str):
        self.df = get_df(db_path)

    def get_ip_data(self, ip: str) -> Dict:
        err = None
        res_dict = dict()
        try:
            ip_int = int(ipaddress.IPv4Address(ip))
        except Exception as e:
            ip_int = None
            err = str(e)
        if ip_int is not None:
            res = self.df[(self.df.ip_to >= ip_int) & (self.df.ip_from <= ip_int)]
            res = res[['country_code', 'country_name', 'region_name', 'city_name']]
            res_dict = res.to_dict('record')[0]
        res_dict['ip'] = ip
        res_dict['error'] = err
        return res_dict


def get_df(path_to_csv: str) -> pd.core.frame.DataFrame:
    if not os.path.exists(path_to_csv):
        raise FileNotFoundError(2, 'No such file or directory', path_to_csv)
    df = pd.read_csv(path_to_csv,
                     names=['ip_from', 'ip_to', 'country_code', 'country_name', 'region_name', 'city_name'],
                     index_col=None)
    return df
