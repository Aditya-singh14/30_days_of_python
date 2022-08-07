term=int(input("Enter a number : "))
if term<0:
    print("Enter positive no. ")
else:
    sum=0
    while(term>0):
        sum=sum+term
        term=term-1
    print("the sum is ", sum)