#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os


def api_runner():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest' 
    #Original Sandbox Environment: 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
      'start':'1',
      'limit':'5',
      'convert':'USD'
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': 'fc8fe976-b35f-4c8e-8fed-def5b2c20729',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        #print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

    
    # Use this if you just want to keep it in a dataframe
#     df2 = pd.json_normalize(data['data'])
#     df2['Timestamp'] = pd.to_datetime('now')
#     df = df.append(df2)
#     x=pd.DataFrame(df)    

    # Use this if you want to create a csv and append data to it
    df = pd.json_normalize(data['data'])
    df['timestamp'] = pd.to_datetime('now')

#     if not os.path.isfile(r'C:\Users\adams\OneDrive\Dokumenty\Python\API_4.csv'):
#         df.to_csv(r'C:\Users\adams\OneDrive\Dokumenty\Python\API_4.csv', header='column_names')
#     else:
#         df.to_csv(r'C:\Users\adams\OneDrive\Dokumenty\Python\API_4.csv', mode='a', header=False)
        
    if not os.path.isfile(r'data/API_4.csv'):
        df.to_csv(r'data/API_4.csv', header='column_names')
    else:
        df.to_csv(r'data/API_4.csv', mode='a', header=False)
    

