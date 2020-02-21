"""Шаблон регулярного выраженя соответсвияпароля"""
import re


PATTERN = '^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z_*%&]{8,12}$'


def test(string):
    """тест"""
    result = re.findall(PATTERN, string)
    if result:
        answer = "Valid password"
    else:
        answer = "Password not valid"
    return answer


print(test('aDs14d'))
print(test('aaGdad3*fs_'))
print(test('aaAAA123'))
