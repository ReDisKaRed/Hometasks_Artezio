"""Модуль комплексных чисел"""


class Complex(object):
    """Класс Complex, который описывает комплексные числа, позволяет их
    складывать, вычитать, умножать, делить и получать модуль."""

    def __init__(self, numbers):
        sep = numbers.split()
        self.complex_number = complex(float(sep[0]), float(sep[-1]))

    def __add__(self, other):
        answer = self.complex_number + other.complex_number
        return "{:.2f}".format(answer)

    def __sub__(self, other):
        answer = self.complex_number - other.complex_number
        return "{:.2f}".format(answer)

    def __mul__(self, other):
        answer = self.complex_number * other.complex_number
        return "{:.2f}".format(answer)

    def __truediv__(self, other):
        answer = self.complex_number / other.complex_number
        return "{:.2f}".format(answer)

    def __abs__(self):
        answer = abs(self.complex_number)
        return "{:.2f}+0.00j".format(answer)


if __name__ == '__main__':
    C = Complex('2 1')
    D = Complex('5 6')
    print("{}\n{}\n{}\n{}\n{}\n{}".format(
        C + D, C - D, C * D, C / D,
        abs(C), abs(D)
    ))
