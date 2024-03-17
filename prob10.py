import random

def SameNumber(lst):
    compLst = []
    sharednum = []

    compLstLength = random.randint(1,9)
    for i in compLstLength:
        compLst.append(random.randint(1.100))

    for i in lst:
        if i in compLst and i not in sharednum:
            sharednum.append(i)

    print(sharednum)

lst = input('Write a list of numbers spereaed by space').split()