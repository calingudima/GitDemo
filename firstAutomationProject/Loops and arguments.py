# loops - control flow programming that will help us execute the code - repeatedly, as many times as we need it too.

# FOR LOOP - a loop that helps to iterate over the object as many times as needed. It goes through a cycle and gets executed.
#
# for number in range(1, 5):   # 0 is number 1 in the list, another example: for number in range(5) - will print 5 times, from 0 zero to 4 four.
#     print("Tojtech")
#     print("lalala", number)  # will print the representation of the number of each line.

#
# for number in range(30):
#     print("Tojtech", number)
#     if number == 2:
#         print("hgiuyhkj")  # at 9:13    ###### BREAK will stop the loop at a certain nr.
#         break
#

for number in range(10):
    print("AAA", number)
    if number == 3:
        print("BBB")
        break

#
# number = 100
# while number > 0:
#     print(number)
#     number = number -1
#     number //= 2


# list = [1, 3, 4]                      # FROM NET EXAMPLE
#
# for val in list:
#     if val == 4:
#         continue
#     print(val)
#


#
# number = 100
# while number > 0:          # infinition repeat until  the condition doesnt become fals the execution will never stop,
#     print(number)          # will repeat as long as the condition is true.
# #   number = number - 1    # will go down minus one (-1 ) until (0) zeero.
#     number //= 2           # will devide by 2 in this order, 100, 50, 25, 12, 6, 3, 1. without decimals until bigger than 0 zero.

# input()          # is a function that will keep runing until we tell it not to

number = input("Enter number: ")

print("The number is : " + number)       # will print number

#


call_attempt = ""
while call_attempt.lower() != "quit":         # upper or lower   # this will lower any Capital leter to lower case and match with initial string.
    call_attempt = input("Enter your call attempt: ")
    print("This is the call atempt: " + call_attempt)


call_attempt = ""
while call_attempt.upper() != "QUIT" and call_attempt.lower() != "quit":        # upper or lower   # this will lower any Capital leter to lower case and match with initial string.
    call_attempt = input("Enter your call attempt: ")
    print("This is the call atempt: " + call_attempt)




call_attempt = ""                                      STRIP  TO REMOVE EXTRA SPace
while call_attempt.upper() != "QUIT ":
    var = call_attempt.strip() != " QUIT "
    call_attempt = input("Enter your call attempt: ")
    print("This is the call atempt: " + call_attempt)


name = "  Good evening "
print(name.lstrip())



name = " gg ddd adafdas   aafdfdw"
print(name.split)            # to search split,, will output into list


year_of_birth = 1991
name = "iuyghj"
print("{}{}{}{}".format("The year of birth is: ", year_of_birth, " ", name))            #method where each {} is an argument



#
year_of_birth = 1991
name = "Bob"
print(" The year of birth is: ", f"{year_of_birth} {name}")       #method where each {} is an argument





