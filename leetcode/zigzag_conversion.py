class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if (numRows >= len(s)) or (numRows < 2):
            return s
        
        m = 2 * numRows - 2
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

            row += s[numRows-1::m]

            return row
        
        else:
            row = s[0]
            for i in range(1, numRows - 1):
                row += s[i]
                if m-i < len(s):
                    row += s[m-i]

            row += s[numRows-1]
            
            return row