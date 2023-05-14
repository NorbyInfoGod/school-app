from src.domain.entity import Grade
from src.repository.repository import StudentRepository, DisciplineRepository, GradeRepository
from src.services.services import GradeServices, StudentServices, DisciplineServices, GeneratorServices
from src.ui.exceptions import *


class CommandUI:
    def __init__(self):
        self._student_repository = StudentRepository()
        self._discipline_repository = DisciplineRepository()
        self._grade_repository = GradeRepository()
        self._services = GeneratorServices(self._student_repository, self._discipline_repository, self._grade_repository)
        self.run_main_menu()
    def run_main_menu(self):
        while True:
            print("1 - Manage Students\n2 - Manage Disciplines\n3 - Grade Studets\n4 - Search  \n5 - Statistics\n")
            try:
                match input("> "):
                    case '1':
                        self.run_manager_menu(self._student_repository, self._grade_repository)
                    case '2':
                        self.run_manager_menu(self._discipline_repository, self._grade_repository)
                    case '3':
                        self.run_grade_menu(self._grade_repository, self._student_repository, self._discipline_repository)
                    case '4':
                        self.run_search_menu(self._student_repository, self._discipline_repository, self._grade_repository)
                    case '5':
                        self.run_statistics_menu(self._grade_repository, self._discipline_repository, self._grade_repository)
                    case _:
                        print("Invalid input")
            except Exception as exc:
                print(exc)
    def run_manager_menu(self, repository, grade_repository):
        if repository == self._student_repository:
            self._services = StudentServices(repository, grade_repository)
        else:
            self._services = DisciplineServices(repository, grade_repository)
        print("1 - Add\n2 - Delete\n3 - Update\n4 - List\n")
        match input("> "):
            case '1':
                self._services.add(int(input("ID: ")), input("Name: "))
            case '2':
                self._services.delete(int(input("ID: ")))
            case '3':
                self._services.update(int(input("Search for ID: ")), input("Change name to: "))
            case '4':
                for item in self._services.list():
                    print(item)
            case _:
                print("! ! ! Invalid input")
    def run_grade_menu(self, grade_repository, student_repository, discipline_repository):
        self._services = GradeServices(grade_repository, student_repository, discipline_repository)
        self._services.assign_grade(int(input("Student ID: ")),int(input("Discipline ID: ")),  int(input("Value: ")))

    def run_search_menu(self, student_repository, discipline_repository, grade_repository):
        print("1 - Search Students\n2 - Search Disciplines\n")
        match input("> "):
            case '1':
                self._services = StudentServices(student_repository, grade_repository)
                for line in (self._services.search(input("> "))):
                    print(line)
            case '2':
                self._services = DisciplineServices(discipline_repository, grade_repository)
                for line in (self._services.search(input("> "))):
                    print(line)
            case _:
                print("! ! ! Invalid input")
    def run_statistics_menu(self, grade_repository, student_repository, discipline_repository):
        self._services = GradeServices(grade_repository, student_repository, discipline_repository)
        print("1 - All students failing at one or more disciplines\n2 - Students with the best school situation, sorted in descending order of their aggregated average\n3 - All disciplines at which there is at least one grade, sorted in descending order of the average grade(s) received by all students\n")
        match input("> "):
            case '1':
                for student_id in self._services.list_failing_students():
                    print(student_id)
            case '2':
                for key, value in self._services.list_sorted_students().items():
                    print(f"{key}: {value}")
            case '3':
                for key, value in self._services.list_sorted_disciplines().items():
                    print(f"{key}: {value}")
            case _:
                print("! ! ! Invalid input")