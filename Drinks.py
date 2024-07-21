print("Hello, Welcome to Alex-IT Coffee!!!!")

name = input("What is your name?\n").capitalize()

if name in ["Ben", "Tim"]:
    evil_status = input("Are you evil? (Yes/No)\n").strip().lower()
    good_deeds = int(input("How many good deeds have you done today?\n"))
    if evil_status == "yes" and good_deeds < 5:
        print("You're not welcome here " + name + ", get out!!!")
        exit()
    else:
        print("Oh, so you're one of those good " + name + "s. Come on in!!")
else:
    print("Hello " + name + ", thank you so much for coming in today.\n\n")

menu = "Black Coffee, Espresso, Latte, Cola, Water"

print(name + ", what would you like from our menu today?\nHere is what we are serving.\n" + menu)

order = input().strip().lower()
price = 0

while order not in ["water", "cola", "espresso", "black coffee", "latte"]:
    print("Sorry, we don't have that here.\nPlease choose something from the menu.")
    order = input().strip().lower()

if order == "water":
    price = 5
elif order == "cola":
    price = 10
elif order == "espresso":
    price = 8
elif order == "black coffee":
    price = 3
elif order == "latte":
    whipped_cream = input("Would you like whipped cream with your latte? (Yes/No)\n").strip().lower()
    if whipped_cream == "yes":
        price = 11
    else:
        price = 4


quantity = int(input("How many drinks would you like?\n"))
total = price * quantity

print("Sounds good " + name + ", we'll have your " + str(quantity) + " " + order + "(s) ready for you in a moment.")
print("Thank you, your total amount is: $" + str(total) + ".")
