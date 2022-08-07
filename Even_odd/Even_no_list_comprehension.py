n=int(input("Enter a range of no.for list : "))
list_=[i for i in range(n+1) if (i%2==0)]
print(list_)

x=int(input("Enter a range of no. for touple : "))
touple_={i for i in range(x+1) if (i%2==0)}
print(touple_)