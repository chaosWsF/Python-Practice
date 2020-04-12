"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function 
that will return true if the ransom note can be constructed from the magazines; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Example:

    canConstruct("a", "b") -> false
    canConstruct("aa", "ab") -> false
    canConstruct("aa", "aab") -> true

Note:
    You may assume that both strings contain only lowercase letters.
"""
from collections import Counter


class Solution:
    def canConstruct1(self, ransomNote, magazine):  # 44ms
        ransomNote = Counter(ransomNote)
        magazine = Counter(magazine)
        for s in ransomNote:
            if s not in magazine:
                return False

            if magazine[s] < ransomNote[s]:
                return False
        
        return True

    def canConstruct2(self, ransomNote, magazine):  # 28ms
        for s in set(ransomNote):
            if ransomNote.count(s) > magazine.count(s):
                return False
        
        return True
