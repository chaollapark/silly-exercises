def Divisors(num):
    lst_num = range(1, num+1)
    dvs_lst = []

    for i in lst_num:
        if num % i == 0:
            dvs_lst.append(i)
        
    print(dvs_lst)

num = int(input("what number do you want: "))
Divisors(num)