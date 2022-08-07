def remove_vowel(string):
    vowel=['a','e','i','o','u']
    result=''
    for i in string:
        if i not in vowel:
            result=''.join(result)
            result=result+i
    print(result)


string=input("Enter string : ")
remove_vowel(string)