from bs4 import BeautifulSoup
import requests
import json


def get_data(symbol):

  headers = {
  'cookie': 'visid_incap_2685215=JqlPAOcUSfiCZMx7Zb4QSYKal2IAAAAAQUIPAAAAAADvwCf1TpQzhhhlUGc6MQ3W; _gcl_au=1.1.111628039.1654102660; _ga=GA1.2.840666844.1654102660; _gid=GA1.2.1641560581.1654102660; display-exit-ad=false; api_call_counter=5; __setuid=CvoWFWKYdzacFHGVxXxzAg==; nlbi_2685215_2552364=kBB1GvSgTFUrY828lPRUDQAAAADYg2pQIycejvSrdZcZVofk; _cbclose=1; _cbclose64035=1; verify=test; SET_COOKIE_POLICY=1.0.0; IPO_Language=English; LstQtLst=DCC|DIF; incap_ses_1526_2685215=e0JncP+DC38V4CTJGHEtFdHSmGIAAAAAg6xfr3WGCjM9SKIHaq1/Ig==; _uid64035=E605CB66.7; _ctout64035=1; landing_url=https://www.settrade.com/C04_02_stock_historical_p1.jsp?txtSymbol=DIF&selectPage=2&max=200&language=en; JSESSIONID=5CB7DCD28C62082ECC0DCE0E23C4A0DB.mispn-stt-www02; route=037cdd24e5bb6f78b355513264cf717c; __setuid=CvoWFWKY2GacFHGVy5yYAg==; incap_ses_1526_2685215=7RlcN2D1+H8etSrJGHEtFQvemGIAAAAA1RiLAXAjslND71k/yD8IWw==; visid_incap_2685215=orAoHt7kTMKo2YdabgkbYmbYmGIAAAAAQUIPAAAAAADAe3tadezI+C/PsJ0FEi9n; JSESSIONID=EF664F8E2EA037A9718BF679BBC0544C.mispn-stt-www01; route=aa755421b72b940dcd57f5553f5ae869'
  }
  url = "https://www.settrade.com/C04_02_stock_historical_p1.jsp?txtSymbol="+symbol+"&selectPage=2&max=200&language=en"
  web_data = requests.get(url, headers=headers)

  soup =BeautifulSoup(web_data.text,'html.parser')
  table = soup.find("table", attrs={"class":"table table-info table-hover"})

  table_head = table.find("thead")
  thead_row = table_head.find("tr")
  thead_cols = thead_row.find_all("th")
  thead_cols = [ele.text.strip() for ele in thead_cols]
  thead_cols.pop(0)

  table_body = table.find("tbody")
  tbody_rows = table_body.find_all("tr")
  data = {}

  for row in tbody_rows:
      cols = row.find_all("td")
      cols = [ele.text.strip() for ele in cols]
      key = cols.pop(0) 
      value = {k:v for k,v in zip(thead_cols,cols)}
      mydict = { key:value}
      data.update(mydict)
      # print(mydict)
      

  # jdict = json.dumps(data)

  return data                  

# a = get_data("DIF")
# b= 1