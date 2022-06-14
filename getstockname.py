# from curses import start_color
from bs4 import BeautifulSoup
import requests
import json
from string import punctuation
from keyword import iskeyword
import re
from bfs4 import get_data

def get_stockname():
  
  url = "http://siamchart.com/stock/"

  payload={}
  headers = {
  'Cookie': 'PHPSESSID=87g1dpnq5nddg5vriqqplqqtn1; bb_lastactivity=0; bb_lastvisit=1654349082; bb_sessionhash=c9ef1908f3fead8f921365fbfd46fe4e'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  soup =BeautifulSoup(response.text,'html.parser')
  divTag = soup.find('div', {'id':'content_body'})
  aTags = divTag.findAll('a')
  thead_cols = [ele.text.strip() for ele in aTags]
  stockNames = [ele.split('(')[0] for ele in thead_cols]
  stockNames.pop(0)
  return stockNames


# a = get_stockname()
# data = {}
# for stock in stockNames:
#   data_info = get_data(stock)
#   data_temp = {stock:data_info}
#   data.update(data_temp)



      
