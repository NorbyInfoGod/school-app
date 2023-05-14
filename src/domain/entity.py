from src.domain.validators import EntityValidator
class Grade:
    def __init__(self,student_id, discipline_id,value):
        self._student_id = student_id
        self._discipline_id = discipline_id
        self._value = value
        self._validator = EntityValidator()
        self._validator.validate_id(student_id)
        self._validator.validate_id(discipline_id)
        self._validator.validate_grade(value)
    @property
    def student_id(self):
        return self._student_id

    @property
    def discipline_id(self):
        return self._discipline_id

    @property
    def value(self):
        return self._value


class Student:
    def __init__(self, id, name):
        self._id = id
        self._name = name
        self._validator = EntityValidator()
        self._validator.validate_id(id)

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def __repr__(self):
        return f"{self._id} {self._name}"


class Discipline:
    def __init__(self, id, name):
        self._id = id
        self._name = name
        self._validator = EntityValidator()
        self._validator.validate_id(id)

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def __repr__(self):
        return f"{self._id} {self._name}"
