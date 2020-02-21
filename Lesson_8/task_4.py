"""Шаблон регулярного выраженя формата времени."""
import re


PATTERN = '\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}[+-]\d{2}:\d{2}'


def test(string):
    """тест"""
    match = re.fullmatch(PATTERN, string)
    answer = (match[0] if match else 'No')
    return answer


print(test('2005-08-09T18:31:42+03:30'))
print(test('20054-08-09T18:31:42+03:30'))
