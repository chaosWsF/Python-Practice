"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.

Example 1:

    Input: haystack = "hello", needle = "ll"
    Output: 2

Example 2:

    Input: haystack = "aaaaa", needle = "bba"
    Output: -1

Clarification:

What should we return when needle is an empty string? This is a 
great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is 
an empty string. This is consistent to C's strstr() and Java's 
indexOf().
"""


class Solution:
    def strStr(self, haystack, needle):
        """
        Using str.find()
        Removing two conditions will slow down the speed.
        """
        if not needle:
            return 0
        
        if not haystack:
            return -1
        
        return haystack.find(needle)

    def strStr2(self, haystack, needle):
        """direct solution"""
        if not needle:
            return 0
        
        if not haystack:
            return -1
        
        m = len(haystack)
        n = len(needle)
        for i in range(m-n+1):
            if haystack[i:i+n] == needle:
                return i
        
        return -1

    def strStr3(self, haystack, needle):
        """KMP (Knuth Morris Pratt)"""
        if not needle:
            return 0
        
        if not haystack:
            return -1
        
        m = len(needle)
        n = len(haystack)

        # preprocessing pattern
        lps = [0]
        prefix_len = 0
        for j in range(1, m):
            if needle[prefix_len] == needle[j]:
                prefix_len += 1
            else:
                while prefix_len > 0 and needle[prefix_len] != needle[j]:
                    prefix_len = lps[prefix_len - 1]    # NOTE better than -= 1, example: "ABABBABABC"
                else:
                    if needle[prefix_len] == needle[j]:
                        prefix_len += 1
            
            lps.append(prefix_len)
        
        # main algorithm
        j = 0
        for i in range(n):
            if haystack[i] == needle[j]:
                if j == m - 1:
                    return i - j
                    # j = lps[j - 1]    # used when finding next
                else:
                    j += 1
            else:                
                while haystack[i] != needle[j] and j > 0:
                    j = lps[j - 1]    # NOTE similar to note above
                else:
                    if haystack[i] == needle[j]:
                        j += 1
            
        return -1
