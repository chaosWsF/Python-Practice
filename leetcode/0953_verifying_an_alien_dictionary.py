"""
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. 
The order of the alphabet is some permutation of lowercase letters. Given a sequence of words written in the 
alien language, and the order of the alphabet, return true if and only if the given words are sorted 
lexicographicaly in this alien language.

Example 1:

    Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
    Output: true
    Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:

    Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
    Output: false
    Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:

    Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
    Output: false
    Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to 
                 lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character 
                 which is less than any other character (More info).

Constraints:
    1. 1 <= words.length <= 100
    2. 1 <= words[i].length <= 20
    3. order.length == 26
    4. All characters in words[i] and order are English lowercase letters.
"""


class Solution:
    def isAlienSorted1(self, words, order):
        d = dict(zip(order, [chr(i + 97) for i in range(26)]))
        words = [''.join([d[x] for x in word]) for word in words]
        for i in range(1, len(words)):
            if words[i] < words[i-1]:
                return False
        
        return True

    def isAlienSorted2(self, words, order):
        d = dict(zip(order, range(26)))
        words = [[d[x] for x in word] for word in words]
        for i in range(1, len(words)):
            if words[i] < words[i-1]:
                return False
        
        return True
    
    def isAlienSorted3(self, words, order):
        d = dict(zip(order, range(26)))
        words_cmp = sorted(words, key=lambda word: [d[x] for x in word])        
        return words_cmp == words
