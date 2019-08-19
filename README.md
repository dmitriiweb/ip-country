# ip-country
An offline tool to get country by IP


## Requirements
- Python >= 3.6
- IP2Location™ LITE IP-COUNTRY-REGION-CITY Database

## Installation

1. Download IP2Location database for IPv4 from [https://lite.ip2location.com/database/ip-country-region-city](here)

2. Install library:

   ```
   pip install ip_country
   ```

   

## Usage

```
>>> from pprint import pprint
>>> from ip_country import IPCountry
>>> ip = IPCountry('/path/to/ipdb.csv')
>>> ip_data = ip.get_ip_data('13.73.96.0')
>>> pprint(ip_data)
{'city_name': 'Melbourne',
 'country_code': 'AU',
 'country_name': 'Australia',
 'error': None,
 'ip': '13.73.96.0',
 'region_name': 'Victoria'}

>>> ip_data = ip.get_ip_data('blah.73.96.0')
>>> pprint(ip_data)
{'error': "Only decimal digits permitted in 'blah' in 'blah.73.96.0'",
 'ip': 'blah.73.96.0'}
```

