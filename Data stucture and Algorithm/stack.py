# from inspect import stack


# Stack-Implemented in lifo order
# Usecase-Function calling in any programming is managed in stack
#        -Undo functionality in any editor uses stack to track down last set of operation

# List as stack
s=[]
s.append(4)
s.append(5)
s.append(6)
s.append(7)
print(s)
s.pop()
print(s)
#Deque as list
from collections import deque
stack=deque()
stack.append("netflix.com")
stack.append("netflix.com/login")
stack.append("netflix.com/home")
stack.append("netflix.com/contacts")
print(stack)
stack.pop()
print(stack)
#making your own stack
class Stack:
    def __init__(self):
        self.container=deque()
    def push(self,val):
        self.container.append(val)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container==0)
    def size(self):
        return len(self.container)
    def show(self):
        print(self.container) 
p=Stack()
p.push(5)
p.push(4)
p.push(3)
p.push(2)
p.show()
p.pop()
p.show()
