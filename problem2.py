def OddEvenOr(num, check):
    if num % check == 0:
        print(f'{num} can be diveded by {check}')
    else:
        print(f'{num} can\'t be diveded by {check}')


num = int(input("What do you want to check"))
check = int(input("Divide by?"))

OddEvenOr(num, check)