def evenizer(lst):
    evenlst = []

    for i in lst:
        if i % 2 == 0:
            evenlst.append(i)

    
    print(evenlst)

lst = input("Put you list here").split()