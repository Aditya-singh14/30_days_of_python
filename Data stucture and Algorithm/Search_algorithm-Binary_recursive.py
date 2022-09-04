def binary_Search_recursive(List,Element,Highest_index,Lowest_index):
    if Highest_index<Lowest_index:
        return -1
    mid_index=(Highest_index + Lowest_index )//2
    mid_number=List[mid_index]
    if mid_number==Element:
        return mid_index
    elif mid_number<Element:
        Lowest_index=mid_index+1
    else:
        Highest_index=mid_index-1
    return binary_Search_recursive(List,Element,Highest_index,Lowest_index)
List=[2,3,4,5,10,40]
Element=10
index=binary_Search_recursive(List,Element,len(List),0)

if index!=-1:
    print("Element is pressent at index ",str(index))
else:
    print("Element is not present in array")
