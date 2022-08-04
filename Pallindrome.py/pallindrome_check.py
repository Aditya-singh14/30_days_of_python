n=int(input("Enter a number to check pallindrome "))
temp=n
reverse=0
while(n>0):
    dig=n%10
    reverse=reverse*10+dig
    n=n//10
if (temp==reverse):
    print("The number is a pallindrome")
else:
    print("Not pallindrome")