"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

    string convert(string s, int numRows);

Example 1:

    Input: s = "PAYPALISHIRING", numRows = 3
    Output: "PAHNAPLSIIGYIR"

Example 2:

    Input: s = "PAYPALISHIRING", numRows = 4
    Output: "PINALSIGYAHRPI"
    Explanation:
        P     I    N
        A   L S  I G
        Y A   H R
        P     I

Example 3:

    Input: s = "A", numRows = 1
    Output: "A"

Constraints:
    1. 1 <= s.length <= 1000
    2. s consists of English letters (lower-case and upper-case), ',' and '.'.
    3. 1 <= numRows <= 1000
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:    # 32ms, 100%
        if (numRows >= len(s)) or (numRows == 1):
            return s
        
        m = 2 * (numRows - 1)
        k = len(s) // m
        if k > 0:
            q = len(s) % m
            row = s[0::m]
            for i in range(1, numRows - 1):
                for j in range(k):
                    row += s[i+j*m] + s[m-i+j*m]

                if (0 < q <= numRows) and (i <= q - 1):
                    row += s[i+k*m]
                elif (q > numRows) and (i < m - q + 1):
                    row += s[i+k*m]
                elif (q > numRows) and (m - q + 1 <= i <= q - 1):
                    row += s[i+k*m] + s[m-i+k*m]

            row += s[(numRows-1)::m]
            return row
        else:
            row = s[0]
            for i in range(1, numRows - 1):
                row += s[i]
                if m - i < len(s):
                    row += s[m-i]

            row += s[numRows-1]
            return row
