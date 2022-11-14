# toitech = ("JobRate" : "Great", "Students" : "Smart")
# print(toitech|4])
#

# temperature = 6
#
# if temperature >= 20:
#     print("Hey it's a great weather outside. Come and play.")
#
# else:
#     print(temperature)
#
# if temperature in range(7, 20): # 20 from this list is exclusive, it will not be considered
#         print("Hey, it's little cold outside")
# elif temperature >= 20:   # here the  ELIF and IF goes against each other.
#     print("Hey, its a great weather")
#
# else:
#     print("It feels like frozen")

# car_color = "red"
#
# if car_color == "blue":
#     print("You have a blue car")
# elif car_color == "black":
#     print("You have a black car")
# elif car_color == "red":
#     print("You have a red car")
#
# else:
#     print("I am not sure")
#


# HOMEWORK

# Change the code the way you want to but don’t go outside of what we’ve covered.

# 1. If all 3 conditions met:      You’re allowed to enter.
#
# 2. If one of the conditions is not met, let’s say height, the message should be:
#                                     Although your age and time of entrance requirements are met,
#                            but the height requirement isn’t. Hence, you’re not allowed to enter.

# 3. If none of the requirements are met then we want to print:
#      “You didn’t meet any of the requirements, please go home.
#
# So this way it will cover the fix on line 14 where it still prints else statement considering that one of the
# conditions met.
#
#
# if age >= 21 and time_of_the_day < 10:
#     print("You're allowed to enter but you should wait until it's 10pm")
# elif height > 6.2:
#     print("You're not allowed to enter even if your age criteria is met")
# else:
#     print("Just go home")
# if age ok, hight ok, time to early print - too early,
# if age - false, - go home
# if age ok,
#
# age = 21
# time_of_the_day = 11
# height = 5
# money = 1000
# #
# if money < 1000:
#     print("NO ENTRY")
# else:
#     if age >= 21 and time_of_the_day >= 10 and height <= 6.2:
#         print("You're allowed to enter")
#     else:
#          if age >= 21 and time_of_the_day <= 10 and height > 6.2:
#             print("You're not allowed to enter even if your age criteria is met")
#          elif age < 21 and height >= 6.2:
#             print("too young and too high")
#          elif height > 6.2:
#              print("You're not allowed to enter even if your age criteria is met")
#          elif time_of_the_day < 10:
#             print("All good, but wait till 10")
#          else:
#             print("AAAAAAAAAAAAAAAAAAAAAAAAAAAA")


age = 18
time_of_the_day = 11
height = 7

if age >= 21 and time_of_the_day >= 10 and height <= 6.2:
    print("You're allowed to enter")
elif age >= 21 and time_of_the_day <= 10 and height > 6.2:
    print("You're not allowed to enter even if your age criteria is met")
elif age < 21 and height >= 6.2:
    print("too young and too high, NO ENTRY")
elif height > 6.2:
    print("You're not allowed to enter even if your age criteria is met")
elif time_of_the_day < 10 and age >= 21:
    print("All good, but wait till 10")
elif height <= 6.2 and time_of_the_day <= 10 and age <= 21:
    print("Even if: Hight - OK, Time- ok but wait, age is RESTRICTED")
elif age <= 21 and time_of_the_day >= 11 and height <= 6.2:
    print("Even if: Time- ok, height- ok, age is RESTRICTED")
else:
    print("GO HOME NOW!")


#
# temperature = 22
#
# if temperature >= 20:
#     print("hot")
# else:
#     if temperature in range(7, 20):
#         print("cold")
#     else:
#         print("temp error")
#

# age = 19
# time_of_the_day = 11
# height = 7
#
# if age >= 21 and time_of_the_day >= 10 and height <= 6.2:
#     print("You can enter, all criteria is met.")
# elif height > 6.2:
#     print("You're not allowed to enter even if your age and time criteria is met")
#
# elif age < 21 and height >= 6.2 and time_of_the_day >= 10:
#     print("Time is good, but age and height is RESTRICTED.")
# elif time_of_the_day < 10 and age >= 21:
#     print("You can enter but wait till 10.")
# elif height <= 6.2 and time_of_the_day <= 10 and age <= 21:
#     print("Height is allowed, TIME- TOO EARLY, AGE IS RESTRICTED")
# elif age <= 21 and time_of_the_day >= 10 and height <= 6.2:
#     print("Time OK, Height OK,  AGE IS RESTRICTED")
# elif age >= 21 and time_of_the_day <= 10 and height > 6.2:
#     print("You're not allowed to enter even if your age and time criteria is met")
#
# else:
#     print("GO HOME NOW!")
