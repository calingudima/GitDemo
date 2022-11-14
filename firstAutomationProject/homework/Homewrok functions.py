



typed_word = ""
while(typed_word.lower) != "":
    typed_word = input("Type something: ")
    print("Your typed word is: " + typed_word)
    if typed_word.lower() == "hack":
        raise Exception("You tried to hack the system")

############################################################
############################################################
############################################################


class Library:

    def sort_one(self, genre, author):
        print(genre, author)

    def sort_one(self, color, pages, age_written):
        print(color, pages, age_written)

obj = Library()
obj.sort_one("white", 100, 1999)

##########################################
##########################################

def method_overriding(type, model):
    print(type, model)

def method_overriding(color, material, volume):
    print(color, material, volume)

obj = method_overriding("black", "wood", 55)












