# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        #approach -1


        curr = node
        print(curr)
        prev=ListNode()
        
        while curr.next!=None:
            curr.val = curr.next.val
            prev=curr
            curr=curr.next
            
        prev.next=None

        ## approach - 2
        
        # node.val = node.next.val
        # node.next = node.next.next
        
        