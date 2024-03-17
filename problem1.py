def ageGuesser(name, age, number):
    years = 100 - age
    for i in range(number):
        print(f'{name}, you have {years} left to live')

name = input("What is your name")
age = int(input("What is you age"))
number = int(input("How many times to print"))

ageGuesser(name, age, number)