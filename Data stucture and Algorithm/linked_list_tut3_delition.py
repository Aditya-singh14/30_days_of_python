class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SingleLinkedList:
    def __init__(self):
        self.head=None

    def display(self):
        temp=self.head
        if self.head is None:
            print("Empty Linked List")
        else:
            temp=self.head
            while temp:
                print(temp.data,"---->",end=" ")
                temp=temp.next

    def Deletion_at_begining(self):
        temp=self.head
        self.head=temp.next
        # temp.head=None
        temp.next=None

    def Deletion_at_end(self):
        temp=self.head.next
        previous=self.head
        while temp.next is not None:
            temp=temp.next
            previous=previous.next
        previous.next=None

    def Deletion_at_position(self,pos):
        temp=self.head.next
        previous=self.head
        for i in range(pos-1):
            temp=temp.next
            previous=previous.next
        previous.next=temp.next


L=SingleLinkedList()
n1=Node(10)
L.head=n1
n2=Node(20)
n1.next=n2
n3=Node(30)
n2.next=n3
n4=Node(40)
n3.next=n4
n5=Node(50)
n4.next=n5

L.Deletion_at_begining()

L.Deletion_at_end()

L.Deletion_at_position(2)

L.display()