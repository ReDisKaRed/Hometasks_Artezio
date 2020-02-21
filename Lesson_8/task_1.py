"""Задание 1"""
import requests


def html_size(address):
    """Функция, которая возвращает размер HTML документа."""
    response = requests.post(address)
    return response.headers['content-length']


if __name__ == '__main__':
    print(html_size('https://www.google.com/'))
