def Palindrome(word):
    palword = ""
    for i in reversed(word):
        palword.append(i)

        print(palword)

word = input("put your word here")

Palindrome(word)