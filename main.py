from functions import *

while True:
	option = input("Option (h for help): ")
	if option == 'h':
		help1()
	elif option == 'a':
		addEmployee()
	elif option == 'd':
		deleteEmployee()		
	elif option == 'u':
		updateEmployee()
	elif option == 'g':
		getEmployee()
	elif option == 'p':
		printAllEmployees()
	elif option == 'gd':
		getDepartment()
	elif option == 'pd':
		printDepartments()
	elif option == 'l':
		loadFile()
	elif option == 's':
		saveProgram()
	elif option == 'q':
		break
