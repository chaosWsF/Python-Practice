"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

Example 2:

    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

Example 3:

    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:

    Input: s = ""
    Output: 0

Constraints:
    1. 0 <= s.length <= 5 * 104
    2. s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = res = 0
        char_loc = {}
        for i in range(len(s)):
            if char_loc.get(s[i], -1) >= start:
                start = char_loc[s[i]] + 1
            else:
                res = max(res, i - start + 1)

            char_loc[s[i]] = i

        return res

    def lengthOfLongestSubstring2(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        ss, res = '', 0
        for i in range(len(s)):
            if s[i] not in ss:
                ss += s[i]
            else:
                res = max(res, len(ss))
                ss = ss[ss.find(s[i])+1:] + s[i]
        
        return max(res, len(ss))
