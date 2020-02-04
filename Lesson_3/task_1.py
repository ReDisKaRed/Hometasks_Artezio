"""функции, которые в качестве единственного аргумента принимают список (или кортеж) целых чисел """


def squared_numbers(values):
    """функция возвращает квадраты элементов коллекции"""
    result = []
    for i in values:
        i = i*i
        result.append(i)
    return result


def even_positions(values):
    """функция возвращает только элементы на четных позициях;"""
    result = []
    for i in range(1, len(values), 2):
        result.append(values[i])
    return result


def cubes_of_even_elements(values):
    """функция возвращает кубы четных элементов на нечетных позициях"""
    odd_elements = []
    cubes = []
    for i in range(0, len(values), 2):
        odd_elements.append(values[i])
    for j in odd_elements:
        if j % 2 == 0:
            cubes.append(j**3)
    return cubes


TUPLE_ARG = (1, 4, 6, 8, 7)
LIST_ARG = [-1, 10, 3, 32, 100, -4]
print("\nFunction: squared numbers. \n")
print(squared_numbers(TUPLE_ARG))
print(squared_numbers(LIST_ARG))
print("\nFunction: even positions. \n")
print(even_positions(TUPLE_ARG))
print(even_positions(LIST_ARG))
print("\nFunction: cubes of even elements. \n")
print(cubes_of_even_elements(TUPLE_ARG))
print(cubes_of_even_elements(LIST_ARG))
