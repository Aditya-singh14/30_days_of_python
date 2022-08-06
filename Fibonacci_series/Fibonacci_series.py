terms=int(input("Enter the no. of terms"))

n1,n2=0,1
count=0

while count<terms:
    print(n1)
    nth=n1+n2
    #update value
    n1=n2
    n2=nth
    count+=1