import unittest

from src.domain.entity import Student
from src.repository.repository import StudentRepository, DisciplineRepository, GradeRepository
from src.services.services import StudentServices

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self._services = StudentServices(StudentRepository(), GradeRepository())

    def test_read(self):
        self.assertEqual(self._services.read(), [])
    def test_add(self):
        self._services.add(12, "don")
        self.assertEqual(self._services.list(), ["12 don"])
    def test_list(self):
        self._services.add(12, "don")
        self.assertEqual(self._services.list(), ["12 don"])
    def test_delete(self):
        self._services.add(12, "don")
        self._services.delete(12)
        self.assertEqual(self._services.list(), [])

    def test_update(self):
        self._services.add(12, "don")
        self._services.update(12, "mark")
        self.assertEqual(self._services.list(), ["12 mark"])

if __name__ == '__main__':
    unittest.main()
