#create employee class with firstname,lastname,pay,email
#create subclass developer,manager
#also print the employees coming under manager, in this also add new employee under manager and remove them
#also use th concept og class varaible to raise the pay of the employee

class Employee:
    raise_amount = 1.04

    def __init__(self,first_name, last_name,pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name+'.'+last_name+'@'+'company.com'

    def get_fullname(self):
        return "{} {}".format(self.first_name,self.last_name)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self,first_name, last_name,pay,prog_lang):
        super().__init__(first_name, last_name,pay)
        self.prog_lang = prog_lang

    def get_details_of_developer(self):
        print("Name:{}\nPay:{}\nProgramming language:{}".format(self.get_fullname(),self.pay,self.prog_lang))

class Manager(Employee):
    def __init__(self,first_name, last_name,pay,employees=None):
        super().__init__(first_name, last_name,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_new_employee(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_all_employees(self):
        print("The following work under :{}".format(self.get_fullname()))
        for eachemp in self.employees:
            print('Employee:', eachemp.get_fullname())

#creation of employees
emp1 = Employee('John','Huzz',50000)
emp2 = Employee('David','Miller',60000)

print("******EMPLOYEE DETAILS******")
print(emp1.get_fullname())
print(emp2.get_fullname())

#creation of developers
dev1 = Developer('Sindhu','S',50000,'Python')
dev2 = Developer('Shruthi','S',60000,'Java')
dev3 = Developer('Nitesh','D',45000,'SCCM')

#printing all details of 2 developers
print("*********DEVELOPER DETAILS*******")
dev1.get_details_of_developer()
dev2.get_details_of_developer()

#print the details of the employess coming under manager which includes adding and removing emoployees
manager1 = Manager('ABC','TOM',90000,[dev1])
manager2 = Manager('XXX','Miller',100000,[dev2])

#printing all the employees under manager
manager1.print_all_employees()
manager2.print_all_employees()

#adding new employee
manager2.add_new_employee(dev3)
manager2.print_all_employees()

#removing employee
manager2.remove_employee(dev3)
manager2.print_all_employees()

print("employees raise amount value:", Employee.raise_amount)
print("Developer1 salary before raise:",dev1.pay)
dev1.apply_raise()
print("Developer1 salary after raise:",dev1.pay)

print("Employee1 salary before raise:",emp1.pay)
emp1.apply_raise()
print("Employee1 salary after raise:",emp1.pay)













