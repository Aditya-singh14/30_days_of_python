class Employee:
    def __init__(self,fname,lname,sal):
        self.firstname=fname
        self.lastname=lname
        self.salary=sal
        Employee.number_of_employee+=1

    @classmethod
    def from_str(cls,emp_string):
        fname,lname,salary=emp_string.split("-")
        return cls(fname,lname,salary)
    
    @staticmethod
    def isopen(day):
        if day=="Sunday":
            return False
        else:
            return True
# shubham=Employee("Shubham","Jackson",88000)    # We dont need to make object from the class , Since it is a static method
print(Employee.isopen("Sunday"))
print(Employee.isopen("Monday"))
# Static methods: A static method is a general utility method that performs a task in isolation.
# Inside this method, we don’t use instance or class variable because this static method doesn’t take any parameters like self and cls.