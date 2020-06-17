# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        ## using recursion 
        if not head or (not head.next):
            return head
        
        smallAns = self.reverseList(head.next)
        tail = head.next  # 1  5-4-3-2  , here actually our 1 is connected to 2 , so we could get tail directly
        tail.next = head # connect 2 with 1
        head.next = None ## make 1.next = none
        head = smallAns # update head
        return smallAns
        
        ## iterative way
#         prev = None
#         curr = head
        
#         while curr is not None:
#             nextp = curr.next
#             curr.next = prev
#             prev = curr
#             curr=nextp
        
#         return prev

    
            
        
        
        