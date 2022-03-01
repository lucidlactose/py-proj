from functions import *

while True:
	option = input("Option (h for help): ")
	if option == 'h':
		_help()
	if option == 'a':
		addEmployee()
	if option == 'd':
		deleteEmployee()		
	if option == 'u':
		updateEmployee()
	if option == 'g':
		getEmployee()
	if option == 'p':
		printAllEmployees()
	if option == 'pd':
		printDepartments()
	if option == 'q':
		break
