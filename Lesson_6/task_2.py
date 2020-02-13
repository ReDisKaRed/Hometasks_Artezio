"""Для 2 задания"""


class Function(object):
    """Класс для проверки задания."""
    name = 'Liza'
    age = 23
    _last_name = 'Sobornova'

    def __init__(self, city):
        self.city = city

    def something(self):
        """Метод для проверки задания."""

    def nothing(self):
        """Метод для проверки задания."""


if __name__ == '__main__':
    A = Function('NN')
    print([arg for arg in dir(Function) if not arg.startswith('_')])
