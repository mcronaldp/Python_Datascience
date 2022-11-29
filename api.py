# We gaan API data binnen halen:
token = '2OMOXIESIMNWFEKE'

# Ik heb package "alphavantage" geinstalleerd, daarna weer verwijder, lijk ik niet nodig te hebben.
# Uitleg json: https://docs.fileformat.com/web/json/#json-example
# API's: https://www.alphavantage.co/documentation/
# Voorbeeld: 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
# Base API: https://www.alphavantage.co/query?
# Parameters:
# function=TIME_SERIES_INTRADAY
# symbol=IBM
# interval=5min
# apikey=demo

import requests
api_call = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=2OMOXIESIMNWFEKE'

requests.get(url=api_call) # We doen een get request
res = requests.get(url=api_call)
print(res)
print(res.apparent_encoding)
print(res.headers)
print(res.history)

# We maken een json object:
print(res.json())

data = res.json()
print(res.request.path_url)

# nu laten we de Apple aandelen zien:
stock = 'AAPL'
api_call = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock}&interval=5min&apikey={token}'
res = requests.get(url=api_call)
print(res.json())

# print(data.sum())
# Installeer package: Pandas en dataframe-to-image
# We gaan een dataframe maken van deze dictionary.
import dataframe_image as dfi
import pandas as pd

pd.dataFrame(data=data)

