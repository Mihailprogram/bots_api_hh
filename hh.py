import pandas as pd
import requests
from pprint import *


URL = "https://api.hh.ru/vacancies"


def week_get(page=0, name_vak='Python', area=3, salary=20000):
    parms = {
        'text': name_vak,
        "area": area,
        'page': page,
        'per_page': 100,
        'salary_from': salary,
        "only_with_salary": True,
        'period': 7,
    }
    try:
        response = requests.get(URL, parms)
    except Exception as eror:
        eror = response.status_code
        raise Exception(f'Eror API {eror}')
    return response.json()


def get_api(page=0, name_vak='Python', area=3, salary=20000):
    """А."""
    parms = {
        'text': name_vak,
        "area": area,
        'page': page,
        'per_page': 100,
        'salary_from': salary,
        "only_with_salary": True,
    }
    try:
        response = requests.get(URL, parms)
    except Exception as eror:
        eror = response.status_code
        raise Exception(f'Eror API {eror}')
    return response.json()


def get_city():
    try:
        url = "https://api.hh.ru/areas"
        response = requests.get(url)
        src = response.json()
    except Exception:
        raise Exception('Ошибка api городов')
    return src


def city_search(name):
    if name == 'Москва':
        return 1
    elif name == 'Санкт Петербург':
        return 2
    try:
        lis = get_city()[0].get('areas')
        for obl in lis:
            for city in obl.get('areas'):
                if city.get('name') == name:
                    return city.get('id')
    except KeyError:
        raise KeyError('Леее')


def pars_name(response):
    if isinstance(response, dict) is not True:
        raise TypeError("Не словарь")
    try:
        list_hh = response.get('items')
        if isinstance(list_hh, list) is not True:
            raise TypeError("Not is list")
    except KeyError:
        raise KeyError('Ошибка доступа')
    return list_hh


def xlm(mas):
    df = pd.DataFrame(
        {
            "Name": mas[0],
            "http": mas[1],
        }
    )
    df.to_excel('./hh.xlsx', index=False)


def week_hh(name_vak, area_city, salary):
    name_area = city_search(area_city)
    mas_url = []
    found = int(get_api(0, name_vak, name_area).get('pages'))
    for i in range(found):
        response = get_api(i, name_vak, name_area, salary)
        list_h = pars_name(response)
        for i in list_h:
            try:
                mas_url.append(i.get('alternate_url'))
            except KeyError:
                raise KeyError('Not kyes')
    return mas_url

def m_hh(name_vak, area_city, salary):
    name_area = city_search(area_city)
    mas = []
    mas_name = []
    mas_url = []
    found = int(get_api(0, name_vak, name_area).get('pages'))
    for i in range(found):
        response = get_api(i, name_vak, name_area, salary)
        list_h = pars_name(response)
        for i in list_h:
            try:
                mas_name.append(i.get('name'))
                mas_url.append(i.get('alternate_url'))
            except KeyError:
                raise KeyError('Not kyes')
    mas.append(mas_name)
    mas.append(mas_url)
    return mas


def main_hh(name, city):
    xlm(m_hh(name, city))


if __name__ == "__main__":
    print(m_hh("Python", "Екатеринбург", 50000))
