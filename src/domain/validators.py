from src.ui.exceptions import IDInvalidException, GradeException

class EntityValidator:
    @staticmethod
    def validate_id(id:int):
        if id<=0:
            raise IDInvalidException(id)
    @staticmethod
    def validate_grade(value):
        if value<1 or value>10:
            raise GradeException(value)