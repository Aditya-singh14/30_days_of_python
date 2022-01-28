def compute_gcd(x,y):
    if x>y:
        small=y
    else:
        small=x
    for i in range(1,small+1):
        if (x%i==0) and (y%i==0):
            gcd=i
    return gcd

num1=int(input("Enter First Number : "))
num2=int(input("Enter Second Number : "))
print("HCF of the number is : ",compute_gcd(num1,num2))