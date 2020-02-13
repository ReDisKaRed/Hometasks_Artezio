"""Итератор"""


class EvenIterator(object):
    """Получает из списка все элементы,
    стоящие на чётных индексах."""

    def __init__(self, lst):
        self.lst = lst
        self.counter = -2

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 2
        if self.counter < len(self.lst):
            return self.lst[self.counter]
        else:
            raise StopIteration


if __name__ == "__main__":
    for l in EvenIterator([1, 4, 6, 'Hello', 'g', '123']):
        print(l)
