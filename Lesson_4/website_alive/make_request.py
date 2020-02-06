"""Импорт библиотеки 'requests'"""
import requests


def site_request(site):
    """Функция делает запрос на сайт"""
    req = requests.get(site)
    return req
