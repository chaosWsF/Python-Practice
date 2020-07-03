"""
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

Example 1:

    Input: "Hello"
    Output: "hello"

Example 2:

    Input: "here"
    Output: "here"

Example 3:

    Input: "LOVELY"
    Output: "lovely"

"""


class Solution:
    def toLowerCase1(self, str):    # 36ms
        return str.lower()

    def toLowerCase2(self, str):    # 24ms
        res = []
        for s in str:
            if 64 < ord(s) < 91:
                res.append(chr(ord(s) + 32))
            else:
                res.append(s)
        
        return ''.join(res)
