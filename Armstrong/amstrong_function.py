# Python program to find a no.  is amstrong no. or not 

#Function to calc x^y
def power(x,y):
    # if x==0:
    #     return 0
    if y==0:
        return 1
    if y%2==0:
        return power(x,y//2)*power(x,y//2)
    return x*power(x,y//2)*power(x,y//2)

def order(x):
    n=0
    while(x!=0):
        n=n+1
        x=x//10
    return n

def isAmstrong(x):
    n=order(x)
    temp=x
    sum=0

    while(temp!=0):
        r=temp%10
        sum=sum + power(r,n)
        temp=temp//10
    return(sum==x)


x=int(input("Enter a num to check armstrong : "))

if isAmstrong(x)==True:
    print(x,"is a Armstrong number ")
else:
    print(x,"is not a Armstrong number ")