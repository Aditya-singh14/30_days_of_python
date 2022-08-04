def Listsort():
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            if (L[i]>L[j]):
                temp=L[i]
                L[i]=L[j]
                [j]=temp
                
L=[5,2,7,3,1,4,6]
