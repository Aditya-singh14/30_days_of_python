class Employee:

    increment=0
    number_of_employee=0

    def __init__(self,fname,lname,sal):
        self.firstname=fname
        self.lastname=lname
        self.salary=sal
        Employee.number_of_employee+=1

    def increase(self):
        self.salary=int(self.salary*self.increment)

    @classmethod
    def change_increment(cls,amount):
        cls.increment=amount

harry=Employee('harry','jackson',44000)
print(harry.salary)