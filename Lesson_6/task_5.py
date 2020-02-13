"""Задание 5"""


def chain(*args):
    """последовательно итерирует переданные объекты"""
    for i in args:
        for j in i:
            yield j


if __name__ == '__main__':
    F_L = [1, 2, ['NAme']]
    S_L = ['df', 123]
    for x in chain(F_L, S_L):
        print(x)
