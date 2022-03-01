from functions import *
import unittest


class TestEmployeeFunctions(unittest.TestCase):

	def test_creation(self):
		addEmployeeWithInfo("1", "Rick", "Astley", "12/32/1900", "1000000", "Music")
		employee = employees[1]
		self.assertEqual(employee.id, "1")
		self.assertEqual(employee.first_name, "Rick")
		self.assertEqual(employee.last_name, "Astley")
		self.assertEqual(employee.DOE, "12/32/1900")
		self.assertEqual(employee.salary, "1000000")
		self.assertEqual(employee.department, "Music")

if __name__ == "__main__":
	unittest.main()
