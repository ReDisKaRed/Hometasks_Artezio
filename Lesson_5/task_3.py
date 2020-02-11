"""Задача 3"""


class Observable(object):
    """Заносит значения как атрибуты."""

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        name = self.__class__.__name__
        attr = ', '.join("{}={}".format(key, val)
                         for key, val in self.__dict__.items() if not key.startswith('_'))
        return '{}({})'.format(name, attr)


class XClass(Observable):
    """Насследник Observable"""
    pass


X = XClass(foo=1, bar=5, _bazz=12, name='Amok', props=('One', 'two'))
print(X)
print(X.foo)
print(X.name)
print(X._bazz)
