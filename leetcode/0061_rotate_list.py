"""
Given the head of a linked list, rotate the list to the right by k places.

Example 1:

    https://assets.leetcode.com/uploads/2020/11/13/rotate1.jpg

    Input: head = [1,2,3,4,5], k = 2
    Output: [4,5,1,2,3]

Example 2:

    https://assets.leetcode.com/uploads/2020/11/13/roate2.jpg

    Input: head = [0,1,2], k = 4
    Output: [2,0,1]

Constraints:
    1. The number of nodes in the list is in the range [0, 500].
    2. -100 <= Node.val <= 100
    3. 0 <= k <= 2 * 10^9
"""


class ListNode:
    """
    Definition for singly-linked list.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:    # 28ms
        if not head:
            return head
        
        n = 1
        cur = head
        while cur.next:
            n += 1
            cur = cur.next
        
        k %= n
        if k == 0:
            return head
        
        back = cur = ListNode()
        for _ in range(n-k):
            cur.next = ListNode(head.val)
            head = head.next
            cur = cur.next

        cur = head
        while cur.next:
            cur = cur.next
        
        cur.next = back.next
        return head
