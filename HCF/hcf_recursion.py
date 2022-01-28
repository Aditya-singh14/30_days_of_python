def hcf(a,b):
    if (b==0):
        return a
    else:
        return hcf(b,a%b)
a=int(input('Enter the value of a:'))
b=int(input('Enter the value of b:'))
print("HCF of ",a,",",b,"is =",hcf(a,b))