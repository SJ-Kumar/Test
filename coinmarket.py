import requests
from requests import Session
import secrets

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': secrets.API_KEY,
}

r = requests.get(url, headers=headers)

class CMC:
    def __init__(self, token):
        self.apiurl = 'https://pro-api.coinmarketcap.com'
        self.headers = headers = { 'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': secrets.API_KEY,
    } 
        self.session = Session()
        self.session.headers.update (headers=headers) 

    def getAllCoins(self):
        url = self.apiurl + 'v1/cryptocurrency/map'
        r = self.session.get(url)
        data = r.json()['data']
        return data

cmc = CMC(secrets.API_KEY)

