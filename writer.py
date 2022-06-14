import imp
import os
from google.cloud import bigquery
from getstockname import get_stockname
from bfs4 import get_data
import json
from datetime import datetime
import numpy as np

credentials_path = "/pythonbq.privatekey.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

client = bigquery.Client()
stockNames = get_stockname()
table_id = 'poetic-park-352312.stock.stockname'
table_stock_info = 'poetic-park-352312.stock.stock'
datas = {}
# # for stock in stockNames:
# data_info = get_data("PTT")
# data_temp = {"PTT":data_info}
# datas.update(data_temp)
# jdict = json.dumps(datas)
# print (type(data_info))
rows_to_insert = [
    # {u'id': 1, u'stockname':'PTT'},
]

i=0
for data in datas:
    for x,y in zip(datas[data].values(),datas[data].keys()):
    # rows_to_insert.append({u'date': data, u'open': data_info[data]["Open"]})
        dto = datetime.strptime(y,'%d/%m/%y').date().isoformat()
        rows_to_insert.append({u'date': dto, u'open': float(x["Open"].replace(',','')), u'high': float(x["High"].replace(',','')),u'low': float(x["Low"].replace(',','')), u'average_price': float(x["Average Price"].replace(',','')), u'close': float(x["Close"].replace(',','')), u'change': float(x["Change"].replace(',','')), u'persentchange': float(x["% Change"].replace(',','')), u'volumex1000': float(x["Volume(x1000)"].replace(',','')), u'volumemb': float(x["Value(MB.)"].replace(',','')), u'setindex': float(x["SETIndex"].replace(',','')),u'id': i, u'stockname':data})
        i+=1
# query_delete = (
#   "DELETE from stockname WHERE id = 1"
# )
# job = client.query(query_delete)
# job.result()
# i=0
# for data in data_temp:
#     rows_to_insert.append({u'date': data.date, u'stockname': stock})
#     i+=1

errors = client.insert_rows_json(table_stock_info, rows_to_insert)
if errors == []:
    print("New rows have been added to the table")
else:
    print("Errors:")
    for error in errors:
        print(error)
