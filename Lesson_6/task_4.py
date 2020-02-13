"""Задание 4"""


def cycle(lst):
    """Циклический итератор"""
    while True:
        for i in lst:
            yield i


if __name__ == '__main__':
    LST = ['a', 2, 'b', 3]
    X = cycle(LST)
    print(next(X))
    print(next(X))
    print(next(X))
    print(next(X))
    print(next(X))
    print(next(X))
    print(next(X))
