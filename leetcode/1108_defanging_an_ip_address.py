"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

Example 1:

    Input: address = "1.1.1.1"
    Output: "1[.]1[.]1[.]1"

Example 2:

    Input: address = "255.100.50.0"
    Output: "255[.]100[.]50[.]0"

Constraints:
    The given address is a valid IPv4 address.
"""


class Solution:
    def defangIPaddr1(self, address: str) -> str:
        return address.replace('.', '[.]')
    
    def defangIPaddr2(self, address: str) -> str:
        res = []
        for s in address:
            if s == ".":
                res.append('[.]')
            else:
                res.append(s)
        
        return ''.join(res)
