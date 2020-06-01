# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        
        even_head = ListNode(0)
        odd_head = ListNode(0)
        even_tail=even_head ## initially head and tail pointing to same node
        odd_tail = odd_head
        checkIsOdd = True
        
        while head:

        	if checkIsOdd:
        		odd_tail.next = head
        		odd_tail = odd_tail.next
        	else:
        		even_tail.next = head
        		even_tail=even_tail.next

        	checkIsOdd=not checkIsOdd
        	head=head.next

        even_tail.next = None
        odd_tail.next = even_head.next
        return odd_head.next



### well python approach is bit different
##  my simple cpp approach is 

'''
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        if(!head){
            return head;
        }
        
       auto odd = head;
       auto even_head=head->next;
        auto even = even_head;
       
        while (even && even->next)
        {
            odd->next = odd->next->next;
            even->next = even->next->next;

            odd = odd->next;
            even = even->next;
        }

        odd->next = even_head;

        return head;
    }
};

            
'''