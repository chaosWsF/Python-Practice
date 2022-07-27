"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

    Input: 1->2
    Output: false

Example 2:

    Input: 1->2->2->1
    Output: true

Follow up:
    Could you do it in O(n) time and O(1) space?
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
            O(n) time and O(1) -> combine two past problems:
                1. fast & slow moving to find loop
                2. reverse linked list
        """
        tortoise = head    # first half
        prev_tortoise = None
        hare = head
        while hare and hare.next:
            hare = hare.next.next
            
            # reversing the first half
            next_tortoise = tortoise.next
            tortoise.next = prev_tortoise
            
            prev_tortoise = tortoise
            tortoise = next_tortoise
        
        if hare:    # odd length
            tortoise = tortoise.next
        
        while tortoise and tortoise.val == prev_tortoise.val:
            tortoise = tortoise.next
            prev_tortoise = prev_tortoise.next
        
        return not prev_tortoise
    
    def isPalindrome1(self, head):
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        
        return stack == stack[::-1]

    def isPalindrome2(self, head):
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        
        for i in range(len(stack) // 2):
            if stack[i] != stack[len(stack)-i-1]:
                return False
        
        return True
