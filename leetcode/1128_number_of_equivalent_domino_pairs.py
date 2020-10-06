"""
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and 
only if either (a==c and b==d), or (a==d and b==c) - that is, one domino can be rotated to 
be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is 
equivalent to dominoes[j].

Example 1:

    Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
    Output: 1

Constraints:
    1. 1 <= dominoes.length <= 40000
    2. 1 <= dominoes[i][j] <= 9
"""

from collections import Counter, defaultdict


class Solution:
    def numEquivDominoPairs(self, dominoes) -> int:    # 232ms
        cnt = Counter([tuple(sorted(x)) for x in dominoes])
        return sum(n * (n-1) // 2 for n in cnt.values())

    def numEquivDominoPairs2(self, dominoes) -> int:    # 212ms
        d = defaultdict(int)
        for a, b in dominoes:
            if a > b:
                a, b = b, a
            
            d[(a, b)] += 1
        
        return sum(n * (n - 1) // 2 for n in d.values())
