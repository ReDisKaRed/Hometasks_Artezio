"""Модуль сведений о стуенте."""


class Student(object):
    """Предоставляет сведения об успешности слушателя некого курса."""

    def __init__(self, name, conf):
        self.name = name
        self.conf = conf
        self.lab_points = self.conf.get('lab_num') * [0]
        self.attempts = self.conf.get('lab_num') * [0]
        self.exam_points = 0
        self.max_attempt = 2

    def make_lab(self, marks, number=-10):
        """Записывает баллы за лабараторные."""
        if number > self.conf.get('lab_num') - 1:
            return self
        if number == -10:
            number = self.lab_points.index(0)
        if self.attempts[number] < self.max_attempt:
            self.attempts[number] += 1
        else:
            return self
        if marks >= self.conf.get('lab_max'):
            marks = self.conf.get('lab_max')
        self.lab_points[number] = marks
        return self

    def make_exam(self, marks):
        """Записывает былла за экзамен."""
        if marks >= self.conf.get('exam_max'):
            marks = self.conf.get('exam_max')
        self.exam_points = marks
        return self

    def is_certified(self):
        """Возвращает сумму баллов студента и оценку."""
        points = sum(self.lab_points) + self.exam_points
        assessment = bool(float(points/100) >= self.conf.get('k'))
        return points, assessment


A = Student('Liza', conf={"exam_max": 30, "lab_max": 7, "lab_num": 10, "k": 0.61})

if __name__ == "__main__":
    A.make_lab(5, 3)
    A.make_lab(7, 3)
    A.make_lab(3, 3)
    A.make_lab(9, )
    A.make_lab(7, )
    print(A.is_certified())
    A.make_lab(7, 8)
    A.make_lab(7, 9)
    A.make_lab(7, 10)
    A.make_exam(50)
    print(A.is_certified())
