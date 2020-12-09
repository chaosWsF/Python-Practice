"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character 
is found. Then, starting from this character takes an optional initial plus or minus sign followed by as many 
numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and 
have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence 
exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:
    1. Only the space character ' ' is considered a whitespace character.
    2. Assume we are dealing with an environment that could only store integers within the 32-bit signed integer 
       range: [−2^31,  2^31 − 1]. If the numerical value is out of the range of representable values, 
       2^31 − 1 or −2^31 is returned.

Example 1:

    Input: str = "42"
    Output: 42

Example 2:

    Input: str = "   -42"
    Output: -42
    Explanation: The first non-whitespace character is '-', which is the minus sign. 
                 Then take as many numerical digits as possible, which gets 42.

Example 3:

    Input: str = "4193 with words"
    Output: 4193
    Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

Example 4:

    Input: str = "words and 987"
    Output: 0
    Explanation: The first non-whitespace character is 'w', which is not a numerical digit or a +/- sign. 
                 Therefore no valid conversion could be performed.

Example 5:

    Input: str = "-91283472332"
    Output: -2147483648
    Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer. Thefore 
                 INT_MIN (−231) is returned.

Constraints:
    1. 0 <= s.length <= 200
    2. s consists of English letters (lower-case and upper-case), digits, ' ', '+', '-' and '.'.
"""


class Solution:
    def myAtoi(self, s: str) -> int:    # 24ms
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        
        if (
            i == len(s) 
            or ((not s[i].isnumeric()) and (s[i] != '-' and s[i] != '+')) 
            or (i == len(s) - 1 and (s[i] == '-' or s[i] == '+'))
        ):
            return 0

        is_neg = False
        if s[i] == '-':
            is_neg = True
            i += 1
        elif s[i] == '+':
            i += 1
        
        res = ''
        for j in range(i, len(s)):
            if s[j].isnumeric():
                res += s[j]
            elif res:
                return max(-int(res), -2**31) if is_neg else min(int(res), 2**31 - 1)
            else:
                return 0

        return max(-int(res), -2**31) if is_neg else min(int(res), 2**31 - 1)
