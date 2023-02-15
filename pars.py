from pprint import pprint
import requests
from bs4 import BeautifulSoup
import lxml
import pandas as pd
import fake_useragent
import json


def len_mas():
    s = requests.Session()
    s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
    r = s.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    mas = soup.find_all('span',class_="pager-item-not-in-short-range")
    max_mas = []
    for i in mas:
        if (i.text).count(".")==0:
            max_mas.append(int(i.text))
    return max(max_mas)

all_vak = []
name = []
vse = []
def pars_hh():
    for i in range(2):
        if i==0:
            url = 'https://ekaterinburg.hh.ru/search/vacancy?no_magic=true&L_save_area=true&text=Python&excluded_text=&area=3&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=20&page=0'
        else:
            url = f'https://ekaterinburg.hh.ru/search/vacancy?no_magic=true&L_save_area=true&text=Python&excluded_text=&area=3&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=20&page={i}'
        # s = requests.Session()
        # s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
        ua = fake_useragent.UserAgent()
        r = requests.get(
            url,
            headers={"user-agent": 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.7 (KHTML, like Gecko) Chrome/2.0.175.0 Safari/530.7'}

        )
        soup = BeautifulSoup(r.content, 'lxml')
        let = soup.find_all("div",class_= "vacancy-serp-item__layout")
        for i in let:
            name1 = i.find('a',class_ = 'serp-item__title')
            name.append(name1.text)
            all_vak.append(name1.get('href'))
    
    vse.append(name)
    vse.append(all_vak)
    return all_vak

URL = "https://api.hh.ru/vacancies"


def get_api(page=0):
    parms = {
        'text': 'Python',
        "area": 3,
        'page': page,
        'per_page': 100,
        "search_field": "name"
    }
    try:
        response = requests.get(URL, parms)
        with open('data.json', 'w',encoding='utf-8') as outfile:
            json.dump(response.json(), outfile,indent=4,ensure_ascii=False)
    except Exception:
        eror = response.status_code
        raise Exception(f'Eror API {eror}')
    return response.json()

def vk_pars():
    token = 'vk1.a.pdU85KCsHduFReb9547sy8hmxlhXsEXZyYrZTk9-OTecQFWBLRTQupIdqLwwJ9KnMbHfarq-cKKAOLhGe9u02jUPpHOhZymerqN7PCBdBk6AMl1ARuBrzPFQJQN1vd9K5jZNr-Rp8DgI9rKOzIseISM0S6Rc2E4i5PoU9hwsMdjdnAi0V3VdhPuLDDcnTriNy8m0mlWYu2ZP8_hR7_NaJQ'
    url = f'https://api.vk.com/method/wall.get?owner_id=296211117&count=137&access_token={token}&v=5.131'
    # ua = fake_useragent.UserAgent()
    resp = requests.get(
        url,
        # headers={"user-agent": ua.random}
    )
    src = resp.json()
    with open('data.json', 'w',encoding='utf-8') as outfile:
        json.dump(src, outfile,indent=4,ensure_ascii=False)
    print(resp.text)

def xlm():   
    a = pars_hh()
    df = pd.DataFrame(
        {
            "Name": a[0],
            "http": a[1], 
        }
    )
    df.to_excel('./hh.xlsx',index=False)

if __name__ =="__main__":
    get_api()