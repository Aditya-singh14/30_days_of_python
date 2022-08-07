def remove_vowel(string_):
    vowel=['a','e','i','o','u']
    
    for i in string_:
        if i in vowel:
            string_=string_.replace(i,"")
    print(string_)

string_=input("Enter any string : ")
remove_vowel(string_)