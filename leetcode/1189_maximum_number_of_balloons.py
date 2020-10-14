"""
Given a string text, you want to use the characters of text to form as many instances of 
the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances 
that can be formed. 

Example 1:

    https://assets.leetcode.com/uploads/2019/09/05/1536_ex1_upd.JPG

    Input: text = "nlaebolko"
    Output: 1

Example 2:

    https://assets.leetcode.com/uploads/2019/09/05/1536_ex2_upd.JPG

    Input: text = "loonbalxballpoon"
    Output: 2

Example 3:

    Input: text = "leetcode"
    Output: 0

Constraints:
    1. 1 <= text.length <= 10^4
    2. text consists of lower case English letters only.
"""

from collections import defaultdict


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = defaultdict(int)
        for s in text:
            cnt[s] += 1
        
        return min(cnt['b'], cnt['a'], cnt['l'] // 2, cnt['o'] // 2, cnt['n'])
