"""
Given a list of strings words representing an English Dictionary, find the longest word in words that can 
be built one character at a time by other words in words. If there is more than one possible answer, return 
the longest word with the smallest lexicographical order. If there is no answer, return the empty string.

Example 1:

    Input: words = ["w", "wo", "wor", "worl", "world"]
    Output: "world"
    Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

Example 2:

    Input: words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    Output: "apple"
    Explanation: Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is 
                 lexicographically smaller than "apply".

Note:
    1. All the strings in the input will only contain lowercase letters.
    2. The length of words will be in the range [1, 1000].
    3. The length of words[i] will be in the range [1, 30].
"""


class Solution:
    def longestWord1(self, words):    # 100ms
        words_set = set(words)
        words.sort(key = lambda s: (-len(s), s))
        for word in words:
            if all(word[:i] in words_set for i in range(1, len(word))):
                return word
        
        return ''

    def longestWord2(self, words):    # 72ms
        words_set = set(words)
        res = ''
        for word in words:
            if len(word) > len(res) or (len(word) == len(res) and word < res):
                if all(word[:i] in words_set for i in range(1, len(word))):
                    res = word
        
        return res
