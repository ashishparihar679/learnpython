class Employee:
    company = "TCS" # class variable
    def __init__(self,emp_name):
        self.emp_name = emp_name #instance variable
    def work(self): # NORMAL INSTANCE METHOD
        print(self.emp_name,"is working")

# OBJECT CREATION
e1=Employee("Ashish")
# e1.work()
# print(Employee.emp_name) AttributeError: type object 'Employee' has no attribute 'emp_name'
print(e1.emp_name)
print(Employee.company)