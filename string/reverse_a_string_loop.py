def reverseString(my_string):
    newStr=''
    for i in my_string:
        newStr=i+my_string
    return newStr

my_string=input("Enter any string : ")
print(reverseString(my_string))