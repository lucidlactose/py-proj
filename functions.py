from Employee import Employee
from Department import Department
from collections import OrderedDict


class UsedIdError(Exception): pass
class TypeIdError(Exception): pass
class MissingIdError(Exception): pass

def _help():
	print("h\t for this menu")
	print("a\t to add an employee")
	print("u\t to update an employee")
	print("g\t to get an employee")
	print("q\t to quit the program")

def addEmployee():
	global employees

	# this while loop was too much work so this is the only place im adding one
	while 1:
		try:
			id = input("Employee Id: ")
			if not id.isnumeric():
				print("raise type")
				raise TypeIdError
			if id in employees[0]:
				print("raise used")
				raise UsedIdError

			first_name = input("First name: ")
			last_name = input("Last name: ")
			DOE = input("Date of Employement: ")
			salary = input("Salary: ")
			department = input("Department: ")
		except TypeError:
			print("Everything except id is a string")
		except UsedIdError:
			print("That id is already used")
		except:
			print("General Error")
		else:
			employee = Employee(id, first_name, last_name, DOE, salary, department)
			employees.append(employee)
			if department not in departments:
				addDepartment(department, 0, 0)
			departments[department].addEmployee(employee)
			employees[0][id] = len(employees) -1
			break

def updateEmployee():
	global employees
	try:
		id = input("Employee Id: ")
		if not id.isnumeric():
			raise TypeError
		if id not in employees[0][id]:
			raise MissingIdError

		first_name = input("First name: ")
		last_name = input("Last name: ")
		DOE = input("Date of Employement: ")
		salary = input("Salary: ")
		department = input("Department: ")

		location = employees[0][id]
		employees[location].udpate(first_name, last_name, DOE, salary, department)
		
	except MissingIdError:
		print("Id does not exist")
	except TypeError:
		print("Only integers pls")
	except:
		print("General Error")

def getEmployee():
	global employees
	try:
		id = input("Employee Id: ")
		if not id.isnumeric():
			raise TypeError
		location = employees[0][id]
		employees[location].info()
		
	except TypeError:
		print("Only integers pls")
	except:
		print("General Error")
	
def deleteEmployee():
	global employees
	try:
		id = input("Employee Id: ")
		if not id.isnumeric():
			raise TypeError
		if id not in employees[0]:
			raise MissingIdError
		location = employees[0][id]
		employees[0].pop(id)
		departments[employees[location]].deleteEmployee(employee)
		employees.pop(location)
		for i in range(1, len(employees)):
			employee_id = employees[i].id
			employees[0][employee_id] = i
		
	except MissingIdError:
		print("Id does not exist")
	except TypeError:
		print("Only integers pls")
	except:
		print("General Error")

def printAllEmployees():
	global employees
	
	print("Id\t|Name\t\t|DOE\t|Salary\t|Department")
	[employees[i].sInfo() for i in range(1, len(employees))]

def getEmployees():
	return [{}]

employees = getEmployees()




















def addDepartment():
	global departments
	name = input("Department name: ")
	budget = input("Department budget: ")
	phone = input("Department phone: ")
	departments[name] = Department(name, budget, phone)

def addDepartment(name, budget, phone):
	departments[name] = Department(name, budget, phone)

def deleteDepartment():
	global departments
	name = input("Department name: ")
	departments.pop(name)

def printDepartments():
	name = input("Department name: ")
	if name in departments:
		departments[name].info()

def getDepartments():
	return OrderedDict()

departments = getDepartments()