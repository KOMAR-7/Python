class Employee:
    def __init__(self,name):
        self.name= name
    
    def __len__(self):
        return len(self.name)
    
    # def getLengthName(self):
    #     return len(self.name)

    def __str__(self):
        return f"The name of employee is str {self.name}"

    def __repr__(self):
        return f"The name of employee is repr {self.name}"

    # def getName(self):
    #     print(f"The name of employee is {self.name}")

    def __call__(self):
        print("I am a call method")

e = Employee("Omar")
print(e)
print(len(e)) # __len__
# print(e.getLengthName())
# print(str(e)) # __len__
# e.getName()
e() # I am a call method