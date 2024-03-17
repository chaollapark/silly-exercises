def SmallerThan(num, list):
    your_numbers = []
    new_list = []
    for j in list:
        new_list.append(int(j))

    for i in list:
        if num > i:
            SmallerThan.append(i)
    
    return your_numbers

num = int(input("The numbe has to be smaller than"))
list = input("A list of numbers you want to compaire").split()

SmallerThan(num, list)