#
# # Create a list of five elements and replace
# the 3rd one with any new element, can also be duplicate,
# update the 5th one, and add 6th element.
#
listOfFive = [1, 2, 3, 4, 5]
print(type(listOfFive))
print(listOfFive)

newnumber = input("Enter nr: ")
newnumber = int(newnumber)
listOfFive[2] = newnumber
print(listOfFive)

print("Updating the 3rd element.")

newnumber2 = input("Enter next nr: ")
newnumber2 = int(newnumber2)
listOfFive[4] = newnumber2
print(listOfFive)

print("Adding the 6th element.")
newnumber3 = input("Enter next nr: ")
newnumber3 = int(newnumber3)
listOfFive.append(newnumber3)
print(listOfFive)
