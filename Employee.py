class Employee:
	def __init__(self, id, first_name, last_name, DOE, salary, department):
		self.id = id
		self.first_name = first_name
		self.last_name = last_name
		self.DOE = DOE
		self.salary = salary
		self.department = department
		"""
		self.values = {
			'id': id,
			'first_name': first_name,
			'last_name': last_name,
			'DOE': DOE,
			'salary': salary,
			'department': department
		}
		"""
	def update(self, first_name, last_name, DOE, salary, department):
		self.first_name = first_name
		self.last_name = last_name
		self.DOE = DOE
		self.salary = salary
		self.department = department
	def info(self):
		print("Id: ", self.id)
		print("Name: ", self.first_name, self.last_name)
		print("Date of Employment: ", self.DOE)
		print("Salary: ", self.salary)
		print("Department: ", self.department)

		"""
		print("Id: ", self.values['id'])
		print("Name: ", self.values['first_name'], self.values['last_name'])
		print("Date of Employment: ", self.values['DOE'])
		print("Salary: ", self.values['salary'])
		print("Department: ", self.values['department'])
		"""
	def sInfo(self):
		print(self.id, f"{self.first_name} {self.last_name}\t", self.DOE, self.salary, self.department, sep='\t|')
