# # # What is the output of the following?
#
pi = 3.14
name = "CodeCrunch"
num = 5
print(type(pi), type(name), type(num))


listOne = [20, 40, 60, 80]
listTwo= [20, 40, 60, 80]
print(listOne == listTwo)
print(listOne is listTwo)






z = [1, 2, 3]
a = z
b = z
print(a == b)
print(a is z)


aTuple = (1, 'Farook', 1 + 3j)
print(type(aTuple[2:3]))


tojtech = "Tojtech" * 2 * 3
print(tojtech)

x = 36 / 4 * (3 + 2) * 4 + 2
print(x)

list2 = [1,2, 2, 2, 3, 4, 5]
set1 = {1, 2, 2, 2, 3, 4, 5}
#set,, is mutuable, is a data type that allows us to store complex objects.
#the only thing is - SET eliminates dublicates.
print(list2)
print(set1)
#
# list2 = [2, 1, 3, 6, 3, 4, 5] # example
# set1 = {2,3,1,6,3,4,5}    # PRINT result will put numbers in numeric order
#
# # set,, is mutuable, is a data type that allows us to store complex objects.
# # the only thing is - SET eliminates dublicates.
# print(list2)
# print(set1)


# CONCATINATION
# CONCATINATION is combining values into ONE and printing into your output, or linking. String to stirng only.

#
# name = "Naseem"
# print("The users name is: " + name) # string plus string
#
# name = "Naseem"
# number = 4
# print("The users name is: " + str(number) + name)  # converting a numbe into string we add ,,str,, plus the rest
# print(type(number))


# DICTIONARY OR DICT
# data type to store multiple objects
#
# dictionary =  {"firstname": "Naseem", "Lastname": "Khalimov", 1: 6}
# print(dictionary)
#
#
# dictionary =  {"firstname": "Naseem", "firstname": "aaa", "Lastname": "Khalimov", 1: 6.5, 2: "Tojtech"}
#  print(dictionary["firstname"])
# print(dictionary["Lastname"])
# print(dictionary[2])
# print(dictionary[1])
#
# dictionary["firstname"] = "Naim" # override data from dictionary initial line
# print(dictionary["firstname"])
# dictionary[1] = 4
# print(dictionary[1])



