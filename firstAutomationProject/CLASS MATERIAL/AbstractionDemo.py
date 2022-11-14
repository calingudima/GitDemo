# ABSTRACTION is a proces of hiding certain implementation
#H iding certain pieces of code from others that are trying to use it.

from abc import ABC, abstractmethod     # abstract base class = abc, ABC class base class

#
# class AbstractClass(ABC)
#     def nigora(self):
#         pass          PASS for an empty body


class AbstractClass(ABC):
    @abstractmethod
    def nigora(self):
        name = "Johny"
        name1 = "Tasha"
        name2 = "Artyom"
        name3 = "Lola"
        name4 = "Ferin"
        print("Hi, welcome to our bootcamp" + " " + name)
        print("Hi, welcome to our bootcamp" + " " +  name1)
        print("Hi, welcome to our bootcamp" + " " +  name2)
        print("Hi, welcome to our bootcamp" + " " +  name3)
        print("Hi, welcome to our bootcamp" + " " +  name4)

    def secret(self):
        x = 150
        y = 160
        print(x, y)

class Tojtech(AbstractClass):
    def nigora(self):
        print("The best bootcamp")


obj = Tojtech()
obj.secret()
obj.nigora()