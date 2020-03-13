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
    def reverseList(self, head):
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
