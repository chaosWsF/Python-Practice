"""
Given a string s, return the longest palindromic substring in s.

Example 1:

    Input: s = "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.

Example 2:

    Input: s = "cbbd"
    Output: "bb"

Example 3:

    Input: s = "a"
    Output: "a"

Example 4:

    Input: s = "ac"
    Output: "a"

Constraints:
    1. 1 <= s.length <= 1000
    2. s consist of only digits and English letters (lower-case and/or upper-case),
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Manacher's Algorithm, O(n)
        https://en.wikipedia.org/wiki/Longest_palindromic_substring#Manacher's_algorithm
        """
        s_transformed = '#'.join('^{}$'.format(s))
        m = len(s_transformed)
        lps = [0] * m
        c = r = max_lps_length = max_lps_center = 0
        for i in range(1, m - 1):
            if i < r:
                lps[i] = min(lps[2 * c - i], r - i)

            while s_transformed[i + lps[i] + 1] == s_transformed[i - lps[i] - 1]:
                lps[i] += 1

            if lps[i] > max_lps_length:
                max_lps_length = lps[i]
                max_lps_center = i

            if i + lps[i] > r:
                c = i
                r = i + lps[i]

        start = (max_lps_center - max_lps_length) // 2
        end = start + max_lps_length
        return s[start:end]

    def longestPalindrome2(self, s: str) -> str:    # very slow
        n = len(s)
        if n > 0:
            for i in range(n, 0, -1):
                for j in range(0, n - i + 1):
                    s_ij = s[j:j+i]
                    if s_ij == s_ij[::-1]:
                        return s_ij
        else:
            return s
