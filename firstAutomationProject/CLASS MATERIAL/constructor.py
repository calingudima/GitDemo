#
#
# class Constructor:
# #    num = 100
#
#
#       def __init__(self, model, year):  # SELF is the object below that is created and stored.
#          print("I will be executed automatically every time an object gets created")
#
#
# obj = Constructor()
# print(obj.num)


class Constructor:
    make = "BMW"

    def __init__(self, model, year):
        self.model = model
        self.year = year
        print(model, year)


obj = Constructor("X5", 2022)    # 10:45 time of explanation
print(obj.make)
object2 = Constructor("Urus", 2022)
