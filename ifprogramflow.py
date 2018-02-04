
age = int(input("How old you are? "))
if age >=18 and age<=60:
    print("You can vote.")
else:
    print("You are not in that age group.")


parrot = "A bird Name"
letter = input("Enter a letter.")
if letter in parrot:
    print("Reward me an {},with money".format(letter))
else:
    print("I don't deserve reward. ")

name = input("Please enter your name: ")
age = int(input("How old you are,{0}? ".format(name)))
if age>=18 and age<40:
    print("Welcome to the Summer holiday club.")
else:
    print("We are sorry you are not in this age group.")


