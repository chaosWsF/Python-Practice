"""
Given head which is a reference node to a singly-linked list. The value of each node in the 
linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

Example 1:

https://assets.leetcode.com/uploads/2019/12/05/graph-1.png

    Input: head = [1,0,1]
    Output: 5
    Explanation: (101) in base 2 = (5) in base 10

Example 2:

    Input: head = [0]
    Output: 0

Example 3:

    Input: head = [1]
    Output: 1

Example 4:

    Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
    Output: 18880

Example 5:

    Input: head = [0,0]
    Output: 0

Constraints:
    1. The Linked List is not empty.
    2. Number of nodes will not exceed 30.
    3. Each node's value is either 0 or 1.
"""


class ListNode:
    """
    Definition for singly-linked list.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = 0
        while head:
            res = 2 * res + head.val
            head = head.next
        
        return res
