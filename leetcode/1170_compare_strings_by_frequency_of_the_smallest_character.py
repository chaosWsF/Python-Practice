"""
Let's define a function f(s) over a non-empty string s, which calculates the frequency of the smallest character in 
s. For example, if s = "dcce" then f(s) = 2 because the smallest character is "c" and its frequency is 2.

Now, given string arrays queries and words, return an integer array answer, where each answer[i] is the number of 
words such that f(queries[i]) < f(W), where W is a word in words.

Example 1:

    Input: queries = ["cbd"], words = ["zaaaz"]
    Output: [1]
    Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").

Example 2:

    Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
    Output: [1,2]
    Explanation: On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa") and f("aaaa") are 
                 both > f("cc").

Constraints:
    1. 1 <= queries.length <= 2000
    2. 1 <= words.length <= 2000
    3. 1 <= queries[i].length, words[i].length <= 10
    4. queries[i][j], words[i][j] are English lowercase letters.
"""

import bisect


class Solution:
    def numSmallerByFrequency(self, queries, words):    # 64ms
        f = lambda s: s.count(min(s))
        f_words, n = sorted([f(s) for s in words]), len(words)
        return [n - bisect.bisect(f_words, f(s)) for s in queries]
