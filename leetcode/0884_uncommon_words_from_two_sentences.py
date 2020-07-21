"""
We are given two sentences A and B. (A sentence is a string of space separated words. Each word consists only 
of lowercase letters.) A word is uncommon if it appears exactly once in one of the sentences, and does not 
appear in the other sentence. Return a list of all uncommon words. You may return the list in any order. 

Example 1:

    Input: A = "this apple is sweet", B = "this apple is sour"
    Output: ["sweet","sour"]

Example 2:

    Input: A = "apple apple", B = "banana"
    Output: ["banana"]

Note:
    1. 0 <= A.length <= 200
    2. 0 <= B.length <= 200
    3. A and B both contain only spaces and lowercase letters.
"""

from collections import Counter


class Solution:
    def uncommonFromSentences(self, A, B):
        d = Counter(A.split() + B.split())
        return [x for x in d if d[x] == 1]
