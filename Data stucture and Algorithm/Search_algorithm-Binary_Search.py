# Binary Search works for sorted array
# We divide the list into two halves if element is present in first halve then ignore the 2nd half and vice-versa

def Binary_Search(arr,element):
    lowest_index=0
    high_index=len(arr)-1
    mid=0
    while lowest_index<=high_index:
        mid=(high_index+lowest_index)//2
        #If x is greater , ignore right half
        if arr[mid]<element:
            lowest_index=mid+1
        #If x is smaller , ignore right half
        elif arr[mid]>element:
            high_index=mid-1
        #It means x is at middle
        else:
            return mid
    return -1
arr=[2,3,4,5,10,40]
element=10
result=Binary_Search(arr,element)
if result!=-1:
    print("Element is pressent at index ", str(result))
else:
    print("Element is not present in array")
        
