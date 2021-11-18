n=int(input("Enter a number: "))
result=1
for i in range(n,0,-1):
    result=result*i
print("The factorial of ",n,"is : ",result)