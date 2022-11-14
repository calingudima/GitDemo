#
# d = 1, 1  # tuple
# print(type(d))
#
# school = "Tojtech"
# print(type(school))  # string
#
# x = 1_000_000_000_000  # Integer can store lots of numbers
# print(x)
#
# c = 5.42335423525235242551   # Float can store lots of nr
# print(c)
#
# tuple1 = (1, 2, 4.6, "string")
# print(tuple1[3])
#
# print(tuple1)  #tuple
# print(type(tuple1)) # tuple example

num1 = 5
num2 = 6
print(num1 > num2)  # boolean example
print(num1 == num2)  # boolean example
print(num1 != num2)

# Boolean == < > and != not equal

# we assign a value to a variable

# TUPLE is a data type that stores multiple items in a single varible. It is not mutuable. It can not be changed.
list2 = [5, 23, 4234, 543, ]
print(list2)

list1 = [1, 2, 3, 22, 4, "TojtechAcademy"]
print(list1[5])  # the dif between TUPLE and LIST is because LIST is mutable, and TUPLE is not mutable.
# 20 sept 10:18 pm , explain the difference.
# The dif between Tuple and List is cos in some cases we SHOULD not be able to change the initial data.
# We use Tuple for that.

list1.remove(22)  # remove tool goes by the name from the list, if its ,, we write 22. or any other value
print(list1)
list1.remove("TojtechAcademy")
print(list1)

list1.insert(2, 10)  # insert goes by the position nr in the list. it will be inserted after the nr we tell.
print(list1)
list1.insert(0, 77)  # number 0 is calculated as a starting nr on the list

list1.append("QA2 2022")  # append adds only a new value at the end of our list, always.
print(list1)

# Create a list of five elements and replace the 3rd one with any new element, can also be duplicate, update the 5th
# one, and add 6th element.

 listnew