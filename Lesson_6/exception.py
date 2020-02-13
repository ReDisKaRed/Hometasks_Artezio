"""Задание по исключениям."""


def func_ex(numbers):
    """Обрабокта исключений."""
    if len(numbers) > 2:
        sep = numbers.split()
        try:
            answer = int(sep[0])/int(sep[1])
        except ValueError as err:
            return "Error Code: {}". format(err)
        except ZeroDivisionError:
            return "Error Code: integer division or modulo by zero"
        else:
            return answer
    else:
        return ''


if __name__ == '__main__':
    print(func_ex('3'))
    print(func_ex('3 1'))
    print(func_ex('3 0'))
    print(func_ex('3 $'))
