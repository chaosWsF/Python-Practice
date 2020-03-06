"""
Reverse bits of a given 32 bits unsigned integer.

Example 1:

    Input: 00000010100101000001111010011100
    Output: 00111001011110000010100101000000
    Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so 
    return 964176192 which its binary representation is 00111001011110000010100101000000.

Example 2:

    Input: 11111111111111111111111111111101
    Output: 10111111111111111111111111111111
    Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so 
    return 3221225471 which its binary representation is 10111111111111111111111111111111.

Note:

    Note that in some languages such as Java, there is no unsigned integer type. In this case, both input and output will be 
    given as signed integer type and should not affect your implementation, as the internal binary representation of the integer 
    is the same whether it is signed or unsigned.

    In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above the input 
    represents the signed integer -3 and the output represents the signed integer -1073741825.

Follow up:
    If this function is called many times, how would you optimize it?
"""


class Solution:
    def reverseBits1(self, n):
        """bin and str, 24ms"""
        tmp = bin(n)[::-1][:-2]
        if len(tmp) < 32:
            tmp += (32 - len(tmp)) * '0'
        return int(tmp, 2)

    def reverseBits2(self, n):
        """bin and int, 24ms"""
        res = 0
        i = 0
        while n > 0:
            res = 2 * res + n % 2
            n >>= 1
            i += 1
        
        if i < 32:
            res <<= 32 - i
        
        return res

    def reverseBits3(self, n):    # bytes.zfill, 24ms
        return int(str(bin(n)[2:].zfill(32)[::-1]), 2)
    
    def reverseBits4(self, n):    # format, 16ms
        return int('{0:032b}'.format(n)[::-1], 2)
