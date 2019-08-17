import unittest

from ip_country import ip_country

DB_PATH = '/home/di/Downloads/ips.csv'


class TestIPCountry(unittest.TestCase):
    def test_ip_country(self):
        ip = '13.35.137.123'
        res = ip_country(DB_PATH, (ip,))
        self.assertEqual(res[0]['Country'], 'Australia')


if __name__ == '__main__':
    unittest.main()
