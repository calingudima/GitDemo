# Conditional statements
# if, elif, else - check if the condition is true or false
# example= requiriment-- Shopping cart can not be empty, please add at least 2 items.

cart = 0

# code identention - 4 spaces before the print in the ,,if block,,

if cart < 2:
    print("The minimum items in the cart should not be less then 2")

# For each ,,if,, we have to add an ,,elif,, condition to make sense in the logic of condition statement.

age = 20
time_of_the_day = 10
height = 6.1

if age >= 21:
    print("Hey, you're allowed to enter our nightclub")

if time_of_the_day >= 10:
    print("You're right on time")
elif time_of_the_day < 10:
    print("It's baby time. Go to bed now")
if height == 6.3:
    print("Your entrance is not allowed, because you wont fit into the door")
elif height < 6.3:
    print("Take Farook's pass and enter, because we just banned him from entrance")
elif age <= 21:
    print("Hey, go to school, what are you doing at the nightclub")

print("Hey, how are you") # this ,,PRINT,, is out of the ,,if block,, so it will be printed regardless of condition.

# range
age = 18

if age in range(22, 59): # if age is set to 59 and range is till 59, no condition will met
    print ("Youre allowed to enter our nightclub")
elif age < 21:
    print("Hey, you're too young to enter")
elif age >= 60:
    print ("You're too old for this club, you might get a heart attack") # this condition is met


credit_score = 600
is_eligible = True

criminal_status = False

if credit_score >= 700:
    print("congratulations, you're approved, but we need aditional verification")

elif not is_eligible:
    print("Hey, even tho your score is matching our expectations, but your eligibility is still under review")


age = 18
time_of_the_day = 19
height = 6.2

# with ,,and,, both conditions should be true

if age >= 21 or time_of_the_day < 10: # instead of ,,or,, also use ,,and,,
    print("you're allowed to enter, but you should wait until it's 10pm")

elif height > 6.2:
    print("You're not allowed to enter if your age criteria is met")

else:
    print("Just go home")


