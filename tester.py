import requests
import random
from random_word import RandomWords

import helper

r = RandomWords()
bid_url = "http://127.0.0.1:5000/"
for x in range(100):
    long_lat = helper.get_random_coords_db()
    params = {"bid_id": random.randint(1,1000),
              "app_id": random.randint(1,1000),
              "app_name" : r.get_random_word(),
              "dev_id": random.randint(1,1000),
              "dev_os": random.choice(helper.mobile_os),
              "dev_country": helper.random_countries(1),
              "dev_long":  long_lat[0],
              "dev_lat": long_lat[1]}

    response = requests.get(bid_url, params=params)
    data = response.json()
    print('For Bid with'+str(params))
    print(data)
