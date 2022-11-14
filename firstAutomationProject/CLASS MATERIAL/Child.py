
# inheritance is used to derive properties from parent class to a child class without changing actual structure of the parent class.

from Inheritance import ParentClass

class ChildClass(ParentClass):
    number1 = 100
    number2 = 200

    def summary_of_all_numbers(self):     # return ChildClass.number1
        return self.number1 + self.number2 + \
               self.summary_of_three_numbers(50, 50, 50) + \
               self.summary_of_two_numbers(100, 200)



obj = ChildClass()

print(obj.summary_of_all_numbers())



# What is the difference between inheritance and abstraction