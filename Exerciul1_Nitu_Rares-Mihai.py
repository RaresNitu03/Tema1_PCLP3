#X=4(Nitu)
#Y=10(Rares-Mihai)

class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        "Displays the number of employees"
        print(f"Total number of employee(s) is {Employee.emp_count}")

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__ (self):
        Employee.empCount -=1

    def update_salary(self, new_salary):
        self.salary = new_salary

##    def add_task(self, task_name):
##        self.tasks[task_name] = "New"   # needs tasks defined before (in __init__)
##
##    def update_tasks(self, task_name, status):
##        self.tasks[task_name] = status
    def modify_task(self, task_name, status="New"):
        self.tasks[task_name]=status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)

class Manager(Employee):
    mgr_count=0
    def __init__(self, nume, salary, departament):
        super().__init__(nume, salary)
        self.departament=departament
        Manager.mgr_count +=1
    
    def display_employee(self):
        print("Salary: ", self.departament)

departament="A05"

manager1=Manager("Nume1", 1000, departament)
manager2=Manager("Nume2", 2000, departament)
manager3=Manager("Nume3", 3000, departament)

manager1.display_employee()
manager2.display_employee()
manager3.display_employee()

employe1=Employee("Nume4", 4000)
employe2=Employee("Nume5", 5000)
employe3=Employee("Nume6", 6000)

employe1.display_employee()
employe2.display_employee()
employe3.display_employee()

print(manager1.mgr_count)
print(employe1.empCount)