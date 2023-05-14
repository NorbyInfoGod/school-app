from src.domain.entity import Grade
from src.domain.validators import EntityValidator
from src.ui.exceptions import IDFoundException, IDInvalidException, IDNotFoundException
import random
class GeneratorServices:

    def __init__(self, student_repository, discipline_repository, grade_repository):
        self._student_repository = student_repository
        self._discipline_repository = discipline_repository
        self._grade_repository = grade_repository
        self.generate()

    def generate(self):
        with open("../../src/services/student_names") as student_input:
            student_list = student_input.read().split("\n")
        with open("../../src/services/discipline_names") as discipline_input:
            discipline_list = discipline_input.read().split("\n")
        i = 0
        while i < 5:
            student_id = random.randint(1,100)
            try:
                student_name = random.choice(student_list)
                self._student_repository.add(student_id, student_name)
                i+=1
            except IDFoundException:
                pass
        i = 0
        while i < 5:
            discipline_id = random.randint(1, 100)
            try:
                discipline_name = random.choice(discipline_list)
                self._discipline_repository.add(discipline_id, discipline_name)
                i+=1
            except IDFoundException:
                pass
        for student in self._student_repository.read():
            for discipline in self._discipline_repository.read():
                for i in range(random.randint(0,4)):
                    self._grade_repository.add(Grade(student.id,discipline.id, random.randint(1,10)))
class StudentServices:
    def __init__(self, student_repository, grade_repository):
        self._student_repository = student_repository
        self._grade_repository = grade_repository
    def add(self, id, name):
        self._student_repository.add(id, name)

    def delete(self, id):
        self._student_repository.delete(id)
        self._grade_repository.delete_student_grades(id)
    def update(self, id, newname):
        self._student_repository.update(id, newname)

    def list(self):
        return self._student_repository.list()

    def __len__(self):
        return self._student_repository.__len__()

    def read(self):
        return self._student_repository.read()
    def search(self, user_input:str):
        result_list = []
        for line in self._student_repository.list():
            if str.upper(user_input) in str.upper(line):
                result_list.append(line)
        return result_list


class DisciplineServices:
    def __init__(self, discipline_repository, grade_repository):
        self._discipline_repository = discipline_repository
        self._grade_repository = grade_repository
    def add(self, id, name):
        self._discipline_repository.add(id, name)

    def delete(self, id):
        self._discipline_repository.delete(id)
        self._grade_repository.delete_discipline_grades(id)
    def update(self, id, newname):
        self._discipline_repository.update(id, newname)

    def list(self):
        return self._discipline_repository.list()

    def __len__(self):
        return self._discipline_repository.__len__()

    def read(self):
        return self._discipline_repository.read()
    def search(self, user_input:str):
        result_list = []
        for line in self._discipline_repository.list():
            if str.upper(user_input) in str.upper(line):
                result_list.append(line)
        return result_list

class GradeServices:
    def __init__(self, grade_repository, student_repository, discipline_repository):
        self._grade_repository = grade_repository
        self._discipline_repository = discipline_repository
        self._student_repository = student_repository
    def assign_grade(self, student_id, discipline_id, value):
        Found_Student, Found_Discipline = False, False
        for student in self._student_repository.read():
            if student.id == student_id:
                Found_Student = True
                break
        if Found_Student is False:
            raise IDNotFoundException(student_id)
        for discipline in self._discipline_repository.read():
            if discipline.id == discipline_id:
                Found_Discipline = True
                break
        if Found_Discipline is False:
            raise IDNotFoundException(discipline_id)
        self._grade_repository.add(Grade(student_id, discipline_id, value))
    def list_failing_students(self):
        return self._grade_repository.list_failing_students()
    def list_sorted_students(self):
        return self._grade_repository.list_sorted_students()
    def list_sorted_disciplines(self):
        return self._grade_repository.list_sorted_disciplines()