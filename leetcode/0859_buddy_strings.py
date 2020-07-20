"""
Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B. 

Example 1:

    Input: A = "ab", B = "ba"
    Output: true

Example 2:

    Input: A = "ab", B = "ab"
    Output: false

Example 3:

    Input: A = "aa", B = "aa"
    Output: true

Example 4:

    Input: A = "aaaaaaabc", B = "aaaaaaacb"
    Output: true

Example 5:

    Input: A = "", B = "aa"
    Output: false

Constraints:
    1. 0 <= A.length <= 20000
    2. 0 <= B.length <= 20000
    3. A and B consist only of lowercase letters.
"""


class Solution:
    def buddyStrings(self, A, B):
        if len(A) != len(B):
            return False
        elif A == B:
            d = set()
            for a in A:
                if a in d:
                    return True
                else:
                    d.add(a)
            
            return False
        else:
            flag, difference = 0, {}
            for i in range(len(A)):
                if A[i] != B[i]:
                    if flag == 0:
                        flag += 1
                        difference[A[i]] = B[i]
                    elif flag == 1:
                        return (B[i] in difference and difference[B[i]] == A[i] and A[i+1:] == B[i+1:])
        
            return False
