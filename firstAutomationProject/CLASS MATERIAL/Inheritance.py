
class ParentClass:
    num1 = 400
    num2 = 500

    def summary_of_two_numbers(self, num1, num2):
        return num1 + num2                        # return - reserved keyword to return back a method or result every time method gets called.

    def summary_of_three_numbers(self, num3, num4, num5):
        return num3 + num4 + num5




obj = ParentClass()
print(obj.summary_of_two_numbers(15, 45))
print(obj.summary_of_three_numbers(20, 40, 60))