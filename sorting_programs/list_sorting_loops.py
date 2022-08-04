L=[5,2,7,3,1,4,6]
NewList=[]
for i in range(len(L)):
    NewList.append(min(L))
    L.remove(min(L))
print(NewList)
