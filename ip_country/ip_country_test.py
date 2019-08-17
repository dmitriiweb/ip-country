import unittest

from ip_country import ip_country, get_df

DB_PATH = '/home/di/Downloads/ips.csv'


class TestIPCountry(unittest.TestCase):
    def test_ip_country(self):
        ip = '13.35.137.123'
        res = ip_country(DB_PATH, (ip,))
        self.assertEqual(res[0]['Country'], 'Australia')

    def test_get_df(self):
        df = get_df(DB_PATH)
        self.assertEqual(df.country_code[1], 'US')

    def test_get_df_err(self):
        with self.assertRaises(FileNotFoundError): get_df('/home/blah')


if __name__ == '__main__':
    unittest.main()
