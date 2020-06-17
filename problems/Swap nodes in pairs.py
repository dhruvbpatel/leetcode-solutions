# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if not head:
            return None
        
        if not head.next:
            return head
        
        
        smallAns = self.swapPairs(head.next.next)
        
        
        temp = head
        head = head.next
        head.next = temp
        
        
        temp.next = smallAns
        
        return head
        
        
        
        
        