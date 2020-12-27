"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

    Input: n = 1
    Output: ["()"]

Example 2:

    Input: n = 2
    Output: ["(())", "()()"]

Example 3:

    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]

Constraints:
    1 <= n <= 8
"""


class Solution:
    def generateParenthesis(self, n: int):
        if n == 1:
            return ['()']
        else:
            return list(set(s[:i]+'()'+s[i:] for s in self.generateParenthesis(n-1) for i in range(1, n+1)))
