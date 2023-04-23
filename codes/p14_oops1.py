# Noun      ->  Class      -> Employee
# Adjective ->  Attributes -> name, age, salary
# Verbs     ->  Methods    -> getSalary(), getAge()

# Create a class
class perfect:
    name="Madi"
# Create an object
p = perfect()
print(p.name)

# Ex2
class flightForm:
    formType="flightForm"
    def printData(self):
        print(f"Name of the person is:{self.name}")
        print(f"Flight of the person is:{self.flight}")

madiApplication = flightForm()
madiApplication.name="Madi"
madiApplication.flight="AirIndia"
madiApplication.printData()


# Class Atrributes
# An attributes that belongs to a class rather than object
class clsAttri:
    company = "Wipro"
madi2 = clsAttri()
print(madi2.company)
clsAttri.company = "Amazon"
print(madi2.company)

# Instance
#  An individual object of a certain class. An object obj that belongs to a class Circle, for example, is an instance of the class Circle. Instantiation − The creation of an instance of a class. Method − A special kind of function that is defined in a class definition.
class employee:
    company = "Infosys"
    salary = 987556

omar = employee()
neuro = employee()
print(omar.company) # Infosys
print(neuro.company) # Infosys

# Create instance attribute
# An instance attribute is a Python variable belonging to only one object.
omar.company = "Google"
print(omar.company) # Google

# Self Parameter:
class employee1:
    company = "TCS"
    # def getSalary(self):
    #     print("Salary is 100k")
    def getSalary(self, signature):
        print(f"Salary of employee working in {self.company} is {self.salary}\n{signature}")

madi1 = employee1()
# employee1.getSalary(madi1)
# madi1.getSalary()
madi1.salary = 1000000
madi1.getSalary("That's Ok")
# you can access the properties of that particular method

# Ex2.
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")

cat1 = Cat('Andy', 2)
cat1.info()
cat2 = Cat('Phoebe', 3)

# The self keyword is used to represent an instance (object) of the given class. In this case, the two Cat objects cat1 and cat2 have their own name and age attributes. If there was no self argument, the same class couldn't hold the information for both these objects.
# However, since the class is just a blueprint, self allows access to the attributes and methods of each object in python. This allows each object to have its own attributes and methods. Thus, even long before creating these objects, we reference the objects as self while defining the class.

# Static Method:
# Static methods in Python are extremely similar to python class level methods, the difference being that a static method is bound to a class rather than the objects for that class. This means that a static method can be called without an object for that class.
class statMet:
   @staticmethod
   def test(status):
      print('static method',status)

# calling a static method without object
statMet.test("Done")
# calling using object
anm = statMet()
anm.test("Done")

# __init__
# Automatically called when the object is created
# Also known as constructor
class person:
    def __init__(self,name):
        print(f"I am created from {name}")

    @staticmethod
    def timeNow():
        print("The time is 9am")

madi3 = person("madi3")
person.timeNow()
# The __init__() function is called automatically every time the class is being used to create a new object.

class employee3:
    company = "Google"
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary


    def getEmployeeDet(self):
        print(f"The employee working in {self.company} is {self.name} which is {self.age} years old who has salary of {self.salary}")

    @staticmethod
    def legalTerm(howMany):
        print(f"{howMany} the employee has accepted all the terms and policy")

# print(employee3.company)
employee3.legalTerm("All")
madi4 = employee3("Omar", 19 , 9876543)
print(madi4.name) # Omar
madi4.getEmployeeDet()

# delete properties
class forDel:
    todel="I will be going soon"
    @staticmethod
    def howTo():
        print("Use del operator and then write the property name you want to delete")

forDel.howTo()
print(forDel.todel)
del forDel.todel
# print(forDel.todel) # error of no property found

# delete Object
# print(forDel) #<class '__main__.forDel'>
# del forDel
# print(forDel) # not defined

# The pass statement
class willUse:
    pass
