"""."""

import collections

class SimpleGradebook(object):
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = []
    
    def report_grades(self, name, score):
        self._grades[name].append(score)

    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)

class Subject(object):
    def __init__(self):
        self._grades = []
    
    def report_grades(self, score, weight):
        Grade = collections.namedtuple('Grade', ('score', 'weight'))
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight

class Student(object):
    def __init__(self):
        self._subjects = {}
    
    def subject(self, name):
        if name not in self._subjects:
            self._subjects[name] = Subject()
        return self._subjects[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count

class Gradebook(object):
    def __init__(self):
        self._students = {}
    
    def student(self, name):
        if name not in self._students:
            self._students[name] = Student()
        return self._students[name]

def main():
    book = SimpleGradebook()
    book.add_student('Isaac Newton')
    book.report_grades('Isaac Newton', 90)
    print(book.average_grade('Isaac Newton'))

    book = Gradebook()
    albert = book.student('Albert Einstein')
    math = albert.subject('Math')
    math.report_grades(80, 0.10)
    print(albert.average_grade())

if __name__ == '__main__':
    main()
