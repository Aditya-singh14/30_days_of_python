class Employee:

    increment=0
    number_of_employee=0

    def __init__(self,fname,lname,sal):
        self.firstname=fname
        self.lastname=lname
        self.salary=sal
        Employee.number_of_employee+=1

    @classmethod
    def from_str(cls,emp_string):
        fname,lname,salary=emp_string.split("-")
        return cls(fname,lname,salary)



harry=Employee('harry','jackson',44000)
print(harry.salary)

lovish=Employee.from_str("Lovish-Jackson-77000")
print(lovish.firstname)
print(lovish.lastname)