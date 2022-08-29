# Queue-It follows fifo criteria

#list as queue
stock_price=[]
stock_price.insert(0,131.10)
stock_price.insert(1,132.12)
stock_price.insert(2,135.00)
stock_price.insert(3,154.4)

print(stock_price)
stock_price.pop()

#Queue using collection
from collections import deque
queuee=deque()
queuee.appendleft(5)
queuee.appendleft(4)
queuee.appendleft(3)
queuee.appendleft(2)
queuee.appendleft(1)
print(queuee)

queuee.pop()
print(queuee)

#Making your own class
class Queue:
    def __init__(self):
        self.buffer=deque()
    def enque(self,val):
        self.buffer.appendleft(val)
    def deque(self):
        return self.buffer.pop()
    def is_empty(self):
        return len(self.buffer)==0
    def size(self):
        return len(self.buffer)
