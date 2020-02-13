"""Задание 3"""


def dict_function(first_list, second_list):
    """Выводит лсоварь."""
    if len(second_list) < len(first_list):
        [second_list.append(None) for i in first_list]
    some_dict = {k: v for k, v in zip(first_list, second_list)}
    return some_dict


if __name__ == '__main__':
    F_L = ['Name', 'age', '123', 768, 'Nik', 'Number']
    S_L = ['Max', '100', 123, 'x']
    print(dict_function(F_L, S_L))
