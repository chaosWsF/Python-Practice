"""
Reverse a singly linked list.

Example:

    Input: 1->2->3->4->5->NULL
    Output: 5->4->3->2->1->NULL

Follow up:
    A linked list can be reversed either iteratively or recursively. Could you implement both?
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Natural solutions (iteratively and recursively)
        """
        # iteratively
        prev = None
        while head:
            next_node = head.next
            head.next = prev

            prev = head
            head = next_node
        
        return prev
        
        # # recursively
        # def helper(prev, cur):
        #     if not cur:
        #         return prev, cur
            
        #     next_node = cur.next
        #     cur.next = prev
        #     return helper(cur, next_node)
        
        # res, _ = helper(None, head)
        # return res
    
    def reverseList1(self, head):
        """recursively"""
        if not (head and head.next):
            return head
        
        res = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return res
    
    def reverseList2(self, head):
        """iteratively"""
        if not head:
            return head
        
        res = ListNode(0)
        while head:
            cur = res.next
            res.next = ListNode(head.val)
            res.next.next = cur
            head = head.next

        return res.next
