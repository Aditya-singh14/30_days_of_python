# Linked List-  It is the chain of nodes, where each node has two fields ~ data and link

# i.e node----node----node----node----null

# -----------   -----------   -----------   -----------
# |Data|Link|---|Data|Link|---|Data|Link|---|Data|Link|     Every node has a single link
# -----------   -----------   -----------   -----------


# [10 |1200]-------------------[20 |1300]---------------------[40 |NULL]
# data=10                      data=20                        data=40
# address of next node=1200    address of next node=1300      address of next node=NULL Since there is no other node after this
# 1st node is also called head                                Last node is also called tail

#Creating a Linkedlist
# In C there is dynamic memory allocation and we have a concept of pointer, but here we do not have pointer, so we have to create class
#with 2 variable i.e data and next address

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None     # Address of next node
class single_Linkedlist:
    def __init__(self):
        self.head=None

# Display Node
    def display(self):
        temp=self.head
        if self.head is None :
            print("Empty Linked List")
        else:
            temp=self.head
            while temp:
                print(temp.data,"--->",end=" ")
                temp=temp.next


L=single_Linkedlist()
n1=Node(10)
L.head=n1
n2=Node(20)
L.head.next=n2
L.display()


