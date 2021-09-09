import requests
import pandas as pd
from datetime import date, timedelta

date_start = str(date.today() + timedelta(days=-1)) + 'T00:00:00Z'
date_end = str(date.today() + timedelta(days=-1)) + 'T23:59:59Z'
file_name_wind = 'Wind_data_' + str(date.today() + timedelta(days=-1))
file_name_consumption = 'Consumption_data_' + str(date.today() + timedelta(days=-1))


PERSONAL_CODE = {"x-api-key": "FNHSaCy1WC2Z6STIgoBaV5wewpzm8HYQ7BlPp3VU"}
time = {'start_time':date_start, 'end_time':date_end}

wind = requests.get('https://api.fingrid.fi/v1/variable/{}/events/json'.format(75), headers=PERSONAL_CODE, params=time)
print(wind.text)

consumption = requests.get('https://api.fingrid.fi/v1/variable/{}/events/json'.format(124), headers=PERSONAL_CODE, params=time)
print(consumption.text)

fileformat = '.json'
wind_file_name = file_name_wind + fileformat
wind_file = open(wind_file_name, 'w')
wind_file.write(wind.text)
wind_file.close()

consumption_file_name = file_name_consumption + fileformat
consumption_data = open(consumption_file_name, 'w')
consumption_data.write(consumption.text)
consumption_data.close()








'''
wind_data = open('wind_data.txt', 'w')
wind_data.write(wind.text)
wind_data.close()

consumption_data = open('consumption_data.txt', 'w')
consumption_data.write(consumption.text)
consumption_data.close()
'''