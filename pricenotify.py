bitcoin_api_url= 'https://api.coinmarketcap.com/v1/ticker/bitcoin'
from urllib import response
import requests

def get_latest_bitcoin_price():
    response = requests.get (bitcoin_api_url)
    response_json = response.json()
    return float (response_json[0]['price_usd'])
    def main():
            price = get_latest_bitcoin_price()
            print ("Bitcoin Price is:"+ price)