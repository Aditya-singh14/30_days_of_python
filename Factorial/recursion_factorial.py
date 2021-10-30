def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

n=int(input("Enter any Number : "))
print("The factorial of",n,"is ",n,"! : ",fact(n))
