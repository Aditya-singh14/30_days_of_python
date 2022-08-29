class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None

    def printrev(self,curr):
        stack=[]
        while curr:
            stack.append(curr)
            curr=curr.next
        while len(stack):
            print(stack.pop().data,"---->",end=" ")
        print("Null")

    def printlist(self,curr):
        while curr:
            print(curr.data,"---->",end=" ")
            curr=curr.next
        print("Null")

    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node

llist=Linkedlist()
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
llist.printlist(llist.head)
llist.printrev(llist.head)