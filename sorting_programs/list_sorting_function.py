def Listsort(L):
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            if (L[i]>L[j]):
                temp=L[i]
                L[i]=L[j]
                L[j]=temp
    return L        
L=[5,2,7,3,1,4,6]

print("sorted list is",Listsort(L))