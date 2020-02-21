"""Задание 2"""
import requests


def rate_calculator(money: float, currency: str, tar_currency: str) -> float:
    """Функция, которая возвращает колчиество денег в целевой валюте."""
    response = requests.post(r'https://api.exchangerate-api.com/v4/latest/{}'.format(currency))
    exchange_rates = response.json()['rates']
    print(exchange_rates)
    answer = money * exchange_rates[tar_currency]
    return round(answer, 2)


if __name__ == '__main__':
    print(rate_calculator(100.00, 'CAD', 'EUR'))
