def vowel(my_string):
    for char in my_string:
        if char in "aeiouAEIOU":
            print(char,end=',')
    return char
my_string=input("Enter any String : ")
vowel(my_string)