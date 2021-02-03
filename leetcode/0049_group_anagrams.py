"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:

    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

    Input: strs = [""]
    Output: [[""]]

Example 3:

    Input: strs = ["a"]
    Output: [["a"]]

Constraints:
    1. 1 <= strs.length <= 104
    2. 0 <= strs[i].length <= 100
    3. strs[i] consists of lower-case English letters.
"""


from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        d = defaultdict(list)
        for s in strs:
            d[''.join(sorted(s))].append(s)
            # d[tuple(sorted(s))].append(s)
        
        return list(d.values())
