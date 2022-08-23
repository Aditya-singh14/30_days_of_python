class Employee:
    increment=1.5
    Number_of_Employee=0
    def __init__(self,fname,lname,sal):
        self.firstname=fname
        self.lastname=lname
        self.salary=sal
        Employee.Number_of_Employee+=1

    def bonus(self):                                         # We can acces the instance of function i.e we can define the increment
        increment=2                                           # variable inside the function
        self.salary=self.salary*increment
        print(harry.salary)

    # def increase(self):                                       # We can access instance of the other function using self.increment
    #     self.salary=self.salary*self.increment

    def increase(self):                                       # We can use instance of the Employee i.e the class itself by using
        self.salary=self.salary*Employee.increment            # Employee.increment which will take the increment var directly from class

harry=Employee("harry","potter",50000)
Aditya=Employee("Aditya", "Singh", 60000)


print(harry.salary)
harry.increase()
# harry.bonus()
print(harry.salary)
print(harry.__dict__)
harry.increment=9
print(harry.__dict__)


# print(Employee.__dict__)
print(Employee.Number_of_Employee)