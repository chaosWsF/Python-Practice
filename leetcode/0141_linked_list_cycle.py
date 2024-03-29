"""
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list 
where tail connects to. If pos is -1, then there is no cycle in the linked list.

Example 1:

    Input: head = [3,2,0,-4], pos = 1
    Output: true
    Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:

    Input: head = [1,2], pos = 0
    Output: true
    Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:

    Input: head = [1], pos = -1
    Output: false
    Explanation: There is no cycle in the linked list.

Follow up:
    Can you solve it using O(1) (i.e. constant) memory?
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle1(self, head):
        """Floyd's Tortoise and Hare (44ms)"""
        if not head:
            return False
        
        tortoise = head
        hare = head.next
        while hare and hare.next and tortoise != hare:
            tortoise = tortoise.next
            hare = hare.next.next

        return tortoise == hare

    def hasCycle2(self, head):
        """Brent's algorithm (40ms)"""
        if not head:
            return False
        
        k = lam = 1
        tortoise = head
        hare = head.next
        while hare and tortoise != hare:
            if lam == k:
                tortoise = hare
                k <<= 2
                lam = 0
            
            hare = hare.next
            lam += 1
        
        return tortoise == hare

    def hasCycle3(self, head):
        """Hashtable (36ms)"""
        d = {}
        while head and (head not in d):
            d[head] = 1
            head = head.next
        return head in d
