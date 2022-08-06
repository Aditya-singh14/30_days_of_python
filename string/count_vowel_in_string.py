string=input("Enter any string : ")
vowel=0
for i in string:
    if i in "aeiouAEIOU":
        vowel=vowel+1
print(vowel)