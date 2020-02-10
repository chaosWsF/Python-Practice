"""
Given a sorted linked list, delete all duplicates such that each 
element appear only once.

Example 1:

    Input: 1->1->2
    Output: 1->2

Example 2:

    Input: 1->1->2->3->3
    Output: 1->2->3
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """direct solution"""        
        cur = head
        while cur:
            val = cur.val
            while cur.next and cur.next.val == val:
                cur.next = cur.next.next
                        
            cur = cur.next

        return head
