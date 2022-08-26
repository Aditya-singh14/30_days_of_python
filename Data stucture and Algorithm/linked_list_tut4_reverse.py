# simple input     Simple Output
# 1                 5
# 5                 4
# 1                 3
# 2                 2
# 3                 1
# 4
# 5

# Method-1
# def reverse(head):
#     #intialise 3 pointer
#     prev=None
#     current=head
#     next=head.next

#     while current!=None:
#         next=current.next
#         current.next=prev
#         prev=current
#         current=next
#     head=prev
#     return head

# Method-2
class Solution:
    def reverselist(self,head):
        prev=None
        while head:
            current=head
            head=head.next
            current.next=prev
            prev=current
        return prev
# curr=1
# head=1               curr=head
# prev=None

# head=head.next
# curr=1
# head=2

# curr.next=prev i.e now 1--->None

