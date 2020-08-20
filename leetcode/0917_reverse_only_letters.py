r"""
Given a string S, return the "reversed" string where all characters that are not a letter stay in 
the same place, and all res reverse their positions.

Example 1:

    Input: "ab-cd"
    Output: "dc-ba"

Example 2:

    Input: "a-bC-dEf-ghIj"
    Output: "j-Ih-gfE-dCba"

Example 3:

    Input: "Test1ng-Leet=code-Q!"
    Output: "Qedo1ct-eeLg=ntse-T!"

Note:
    1. S.length <= 100
    2. 33 <= S[i].ASCIIcode <= 122 
    3. S doesn't contain \ or "
"""


class Solution:
    def reverseOnlyLetters1(self, S):
        res = []
        i = len(S) - 1
        for s in S:
            if s.isalpha():
                while not S[i].isalpha():
                    i -= 1
                
                res.append(S[i])
                i -= 1
            else:
                res.append(s)

        return ''.join(res)

    def reverseOnlyLetters2(self, S):
        letters = [s for s in S if s.isalpha()]
        res = []
        for s in S:
            if s.isalpha():
                res.append(letters.pop())
            else:
                res.append(s)
        
        return ''.join(res)
