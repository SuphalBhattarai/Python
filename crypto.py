#!/usr/bin/env python


import json
import http
import requests


API_KEY = ""
CLIENT_ID = ""
CLIENT_SECRET = ""


def get_previously_saved_data():
    with open("~/.config/crypto/config.json") as f:
        data = json.dumps(f)
    return data.price
        

class Crypto:
    def __init__(self):
        self.API_KEY = API_KEY
        self.CLIENT_SECRET = CLIENT_SECRET
        self.CLIENT_ID = CLIENT_ID


    def get_data_from_api(self): 
        return price

    
    def sell_crypto(self):
        pass


    def buy_crypto(self):
        pass


def main():
    price_old = get_previously_saved_data()
    price_current = Crypto.get_data_from_api(0,0,0)
    
    if price_old < price.current:
            Crypto.sell_crypto()
    if price_old > price_current:
        if check_available_balance = True:
            Crypto.buy_crypto()


if __name__ == "__main__":
    main()
