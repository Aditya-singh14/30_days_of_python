# Class is used as a template for declaring and creating the objects. 
class MyClass:
  x = 5

print(MyClass)

class My2ndclass:
    pass
print(My2ndclass)


# An object is an instance of a class.
class MeraClass:
    x=2
p1 = MeraClass()
print(p1.x)

class Employee:
    pass
harry=Employee()
rohan=Employee()

harry.fname="Harry"                     
harry.lname="Pottor"                # Attributes of class harry
harry.salary="44000"                    

rohan.fname="Rohan"                 # Attributes of class rohan    
rohan.lname="lname"                         
rohan.salary="50000"

print(harry,rohan)                  #There are 2 object


# Condructor:Constructors are generally used for instantiating an object. 
# The task of constructors is to initialize(assign values) to the data members of the class when an object of the class is created.
class Employee:
    def __init__(self,fname,lname,salary):                  #
        self.firstname=fname                                # This is the template
        self.lastname=lname                                 # self.firstname , self.lastname , self.employeesalary are the variables
        self.employeesalary=salary
harry=Employee("harry","jackson",44000)
rohan=Employee("rohan","das",60000)

print(harry,rohan)