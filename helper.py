import random
import requests
import json


def random_countries(n):
    countries = []
    for x in range (0, n):
        countries.append(countries_arr[random.randint(1,5)][1])
    return countries

def random_coords(n):
    coords = []
    for x in range (0, n):
        coords.append((random.random()*2.0, random.random()*2.0))
    return coords

def get_random_coords_db():
    api_url = "http://127.0.0.1:5001/random_loc"

    response = requests.get(api_url)
    coords = response.json()
    return coords


mobile_os = [ "Android", "iOS"]

countries_arr = [
    ('US', 'United States'),
    ('AR', 'Argentina'),
    ('AM', 'Armenia'),
    ('AW', 'Aruba'),
    ('AU', 'Australia'),
    ('DE', 'Germany'),
    ('GH', 'Ghana'),
    ('GI', 'Gibraltar'),
    ('GR', 'Greece'),
    ('HU', 'Hungary'),
    ('IS', 'Iceland'),
    ('IN', 'India'),
    ('ID', 'Indonesia'),
    ('IR', 'Iran'),
    ('IQ', 'Iraq'),
    ('IE', 'Ireland'),
    ('IL', 'Israel'),
    ('IT', 'Italy'),
    ('JM', 'Jamaica'),
    ('JP', 'Japan'),
    ('JO', 'Jordan'),
    ('KZ', 'Kazakhstan'),
    ('LY', 'Libya'),
    ('LI', 'Liechtenstein'),
    ('LT', 'Lithuania'),
    ('MY', 'Malaysia'),
    ('MV', 'Maldives'),
    ('ML', 'Mali'),
    ('MT', 'Malta'),
    ('MX', 'Mexico'),
    ('FM', 'Micronesia'),
    ('MD', 'Moldova'),
    ('NG', 'Nigeria'),
    ('QA', 'Qatar'),
    ('RO', 'Romania'),
    ('RU', 'Russian Federation'),
    ('SG', 'Singapore'),
    ('SK', 'Slovakia'),
    ('SI', 'Slovenia'),
    ('UA', 'Ukraine'),
    ('AE', 'United Arab Emirates'),
    ('UK', 'United Kingdom')
]
