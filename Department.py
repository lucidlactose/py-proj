class Department:
	def __init__(self, name, budget, phone):
		self.name = name
		self.budget = budget
		self.phone = phone
		self.employees = {}

	def addEmployee(self, employee):
		# I guess I could check if the employee is an employee and assert it
		self.employees[employee.id] = employee

	def deleteEmployee(self, employee):
		# I guess I could check if the employee is an employee and assert it
		self.employees.pop(employee)

	def updateDepartment(self, name, budget, phone):
		self.name = name
		self.budget = budget
		self.phone = phone

	def info(self):
		print("Department: ", self.name)
		print("Budget: ", self.budget)
		print("Employee List: ")
		print("Id\t|Name\t\t|DOE\t|Salary")
		[employee.sInfo() for key, employee in self.employees.items()]
