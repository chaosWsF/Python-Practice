"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?

Example 1:

    https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg

    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]

Example 2:

    Input: head = [1], n = 1
    Output: []

Example 3:

    Input: head = [1,2], n = 1
    Output: [1]

Constraints:
    1. The number of nodes in the list is sz.
    2. 1 <= sz <= 30
    3. 0 <= Node.val <= 100
    4. 1 <= n <= sz
"""


import copy


class ListNode:
    """
    Definition for singly-linked list.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        Two Pass
        """
        if not head.next:
            return 
        
        l, cur = 1, head
        while cur.next:
            l += 1
            cur = cur.next

        if l == n:
            return head.next
        
        i, cur = 1, head
        while cur and cur.next:
            if i == l - n:
                cur.next = cur.next.next
            else:
                cur = cur.next
            
            i += 1
        
        return head
    
    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        """
        One Pass, keeping a window with size = n
        """
        if not head.next:
            return 
        
        left = right = head
        i = 0
        while i < n:
            right = right.next
            i += 1
        
        if not right:
            return head.next
        
        while right.next:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return head
