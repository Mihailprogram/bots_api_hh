import requests
from pprint import *

URL = '	https://api.superjob.ru/2.0/vacancies/'

UTL = 'https://api.superjob.ru/2.0/oauth2/access_token/?code=9ba5bfdd2c07b71753b6153118df88c995ee36f453902ff10b3950d87cee0aa8.189d2970044c4cf5c9a3a887c467f997efc85e0a&redirect_uri=http%3A%2F%2Fwww.example.ru&client_id=2580&client_secret=v3.r.137607305.f49266735db0e80af33f970306a21b38b1ab235a.d1608b3612c2f2ba4b7f98d384c03fe24f35aa99'

TOKEN = 'v3.r.137607305.f1b4421ad23ab48cd5eb27097414c6116825054d.8892a26bf44ab49939fffb6171da702582b181dd'
HEADERS = { #'Authorization': f'Bearer {TOKEN}',
            "X-Api-App-Id": 'v3.r.137607305.f49266735db0e80af33f970306a21b38b1ab235a.d1608b3612c2f2ba4b7f98d384c03fe24f35aa99'}


def get_prof(name, city, salary):
    parms = {
        'keyword': name,
        'town': city,
        "payment_value": salary,
    }
    resp = requests.get(URL, headers=HEADERS, params=parms)
    vacancies = resp.json()['objects']
    arr = []
    for vacancy in vacancies: 
        arr.append(vacancy['link'])
    return arr
