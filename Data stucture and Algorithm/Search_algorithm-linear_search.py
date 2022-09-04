# Search function with parameter list name
# and the value to be searched

def find(List,a):
    for i in range (len(List)):
        if List[i]==a:
            return i
    

# list which contains both string and numbers.
List = [1, 2, 'sachin', 4, 'Geeks', 6]

# Driver Code
a = 'Geeeks'

if find(List, a):
	print("Found")
else:
	print("Not Found")


# Method 2
def LinearSearch(List,num_to_find):
    for index,element in enumerate(List):   #enumerate returns both index and element 
        if element==num_to_find:
            return index
    return -1 

num_to_find=4
index=LinearSearch(List,num_to_find)
print(f"Number found at index {index} using Linear Search")