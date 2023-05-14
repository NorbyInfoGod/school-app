from src.domain.entity import Student, Discipline, Grade
from src.ui.exceptions import IDFoundException, IDNotFoundException


class GradeRepository:
    def __init__(self):
        self._data = {}

    def add(self, grade):
        if str(grade.discipline_id) not in self._data.keys():
            self._data[str(grade.discipline_id)] = {}
        if str(grade.student_id) not in self._data[str(grade.discipline_id)].keys():
            self._data[str(grade.discipline_id)][str(grade.student_id)] = []
        self._data[str(grade.discipline_id)][str(grade.student_id)].append(grade.value)
    def delete_student_grades(self, student_id):
        for discipline_id in self._data:
            self._data[str(discipline_id)].pop(str(student_id))
    def delete_discipline_grades(self, discipline_id):
        self._data.pop(str(discipline_id))
    def compute_student_average(self, discipline_id, student_id):
        return round(
            sum(self._data[str(discipline_id)][str(student_id)]) / len(self._data[str(discipline_id)][str(student_id)]))

    def list_failing_students(self):
        failing_students = []
        for discipline_id in self._data:
            for student_id in self._data[str(discipline_id)]:
                if self.compute_student_average(discipline_id, student_id) < 5 and student_id not in failing_students:
                    failing_students.append(student_id)
        return failing_students

    def list_sorted_students(self):
        dict_students = {}
        for discipline_id in self._data:
            for student_id in self._data[str(discipline_id)]:
                if str(student_id) not in dict_students.keys():
                    dict_students[str(student_id)] = []
                dict_students[str(student_id)].append(self.compute_student_average(discipline_id, student_id))
        for student_id in dict_students:
            if dict_students[str(student_id)] != []:
                dict_students[str(student_id)] = round(sum(dict_students[str(student_id)]) / len(dict_students[str(student_id)]),2)
        return dict(sorted(dict_students.items(), key=lambda item: item[1], reverse=True))

    def list_sorted_disciplines(self):
        dict_disciplines = {}
        for discipline_id in self._data:
            if str(discipline_id) not in dict_disciplines.keys():
                dict_disciplines[str(discipline_id)] = []
            for student_id in self._data[str(discipline_id)]:
                if sum(self._data[str(discipline_id)][str(student_id)]) != 0:
                    dict_disciplines[str(discipline_id)].append(self.compute_student_average(discipline_id, student_id))
        for discipline_id in dict_disciplines:
            dict_disciplines[str(discipline_id)] = round(sum(dict_disciplines[str(discipline_id)]) / len(
                dict_disciplines[str(discipline_id)]),2)
        return dict(sorted(dict_disciplines.items(), key=lambda item: item[1], reverse=True))


class StudentRepository:
    def __init__(self):
        self._data = []

    def add(self, id, name):
        for student in self._data:
            if student.id == id:
                raise IDFoundException(id)
        self._data.append(Student(id, name))

    def get_student_index_by_id(self, id):
        index = 0
        for student in self._data:
            if student.id == id:
                return index
            index += 1
        raise IDNotFoundException(id)

    def delete(self, id):
        self._data.pop(self.get_student_index_by_id(id))

    def update(self, id, newname):
        self._data[self.get_student_index_by_id(id)].name = newname

    def list(self):
        list = []
        for student in self._data:
            list.append(student)
        return list

    def __len__(self):
        return len(self._data)

    def read(self):
        return self._data


class DisciplineRepository:
    def __init__(self):
        self._data = []

    def add(self, id, name):
        for discipline in self._data:
            if discipline.id == id:
                raise IDFoundException(id)
        self._data.append(Discipline(id, name))
    def get_discipline_index_by_id(self, id):
        index = 0
        for discipline in self._data:
            if discipline.id == id:
                return index
            index += 1
        raise IDNotFoundException(id)

    def delete(self, id):
        self._data.pop(self.get_discipline_index_by_id(id))

    def update(self, discipline, newname):
        discipline.name(newname)

    def list(self):
        list = []
        for discipline in self._data:
            list.append(discipline)
        return list

    def __len__(self):
        return len(self._data)

    def read(self):
        return self._data
