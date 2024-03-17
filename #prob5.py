import random

def MatchingNum(lst):
    
    intlst = []
    lstONE = random.randint(0,10)
    # intlst = [int(num) for num in lst]
    for number in lst:
        intlst.append(int(number))
        
    Overlap = []
    
    for num in lstONE:
        if num in intlst:
            Overlap.append(num)
            print(Overlap)

lst = input("Write the numbers in your list: ").split()

MatchingNum(lst)