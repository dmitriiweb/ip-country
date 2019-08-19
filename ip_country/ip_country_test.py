import unittest

from ip_country import IPCountry, get_df

DB_PATH = '/home/di/Downloads/ips.csv'
IP = '13.73.96.0'


class TestIPCountry(unittest.TestCase):
    def setUp(self):
        self.ic = IPCountry(DB_PATH)

    def test_get_ip_data(self):
        res = self.ic.get_ip_data(IP)
        self.assertEqual(res['country_name'], 'Australia')


class TestGetDF(unittest.TestCase):
    def test_get_df(self):
        df = get_df(DB_PATH)
        self.assertEqual(df.country_code[1], 'US')

    def test_get_df_err(self):
        with self.assertRaises(FileNotFoundError):
            get_df('/home/blah')


if __name__ == '__main__':
    unittest.main()
