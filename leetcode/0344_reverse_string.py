"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

Example 1:

    Input: ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]

Example 2:

    Input: ["H","a","n","n","a","h"]
    Output: ["h","a","n","n","a","H"]
"""

class Solution:
    def reverseString1(self, s):  # 204ms
        s[:] = s[::-1]

    def reverseString2(self, s):  # 196ms
        s.reverse()

    def reverseString3(self, s):  # 196ms
        head = 0
        tail = len(s) - 1
        while head < tail:
            tmp = s[head]
            s[head] = s[tail]
            s[tail] = tmp
            head += 1
            tail -= 1
