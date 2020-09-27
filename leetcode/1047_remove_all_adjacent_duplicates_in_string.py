"""
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent 
and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed the 
answer is unique.

Example 1:

    Input: "abbaca"
    Output: "ca"
    Explanation: 
        For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, 
        and this is the only possible move.  The result of this move is that the string is "aaca", 
        of which only "aa" is possible, so the final string is "ca".

Note:
    1. 1 <= S.length <= 20000
    2. S consists only of English lowercase letters.
"""


from string import ascii_lowercase


class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for s in S:
            if stack and stack[-1] == s:
                stack.pop()
            else:
                stack.append(s)
        
        return ''.join(stack)

    def removeDuplicates2(self, S: str) -> str:
        """
        faster
        """
        d = {2 * letter for letter in ascii_lowercase}
        prev = -1
        while len(S) != prev:
            prev = len(S)
            for letter in d:
                S = S.replace(letter, '')
        
        return S
