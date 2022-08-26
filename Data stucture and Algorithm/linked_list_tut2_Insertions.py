#[10 |1200]-------------------[20 |1300]---------------------[40 |NULL]
#1100                         1200                            1300

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Single_LinkedList:
    def __init__(self):
        self.head=None

    #insertion at begining
    def insert_at_begining(self,data):
        new_node=Node(data)    #Step1-Create a node i.e to be inserted
        new_node.next=self.head   #Step2-address of current 1st node is linked to new nodes
        self.head=new_node

    #insertion at end
    def insert_at_end(self,data):
        new_node=Node(data)    #Step1-Create a node i.e to be inserted
        temp=self.head
        while temp.next:       #Step1-First we have to traverse till the last node
            temp=temp.next
        temp.next=new_node     #Step2-Establish relation between address of last node and new last node

    #insert at any index or position
    def insert_position(self,pos,data):
        new_node=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        new_node.data=data
        new_node.next=temp.next
        temp.next=new_node

    #Display a linked list
    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"--->",end=" ")
                temp=temp.next
L=Single_LinkedList()
n1=Node(10)
L.head=n1
n2=Node(20)
n1.next=n2
n3=Node(30)
n2.next=n3


L.insert_at_begining(5)
L.insert_at_end(19)

L.insert_position(3,25)
L.display()