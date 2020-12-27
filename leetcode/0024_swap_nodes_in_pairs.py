"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes. Only nodes itself may be changed.

Example 1:

    https://assets.leetcode.com/uploads/2020/10/03/swap_ex1.jpg

    Input: head = [1,2,3,4]
    Output: [2,1,4,3]

Example 2:

    Input: head = []
    Output: []

Example 3:

    Input: head = [1]
    Output: [1]

Constraints:
    1. The number of nodes in the list is in the range [0, 100].
    2. 0 <= Node.val <= 100
"""


class ListNode:
    """
    Definition for singly-linked list.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs1(self, head: ListNode) -> ListNode:    # slower
        cur = res = ListNode()
        while head:
            if not cur.next:
                cur.next = ListNode()
            
            cur = cur.next
            if head.next:
                cur.val = head.next.val
                cur.next = ListNode(head.val)
                head = head.next.next
                cur = cur.next
            else:
                cur.val = head.val
                return res.next

        return res.next
    
    def swapPairs(self, head: ListNode) -> ListNode:    # faster
        if head and head.next:
            head.val, head.next.val = head.next.val, head.val
            self.swapPairs(head.next.next)

        return head
