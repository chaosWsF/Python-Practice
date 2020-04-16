"""
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Example:

    Input: n = 1
    Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]

Note:
    The order of output does not matter.
    The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
    The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".
"""
from itertools import combinations


class Solution:
    def readBinaryWatch1(self, num):
        if num == 0:
            return ['0:00']
        elif num > 8:
            return []
        
        res = []
        for ones_index in combinations(range(10), num):
            basis = ['0'] * 10
            for i in ones_index:
                basis[i] = '1'
            
            s = ''.join(basis)
            hour_num = int(s[:4], 2)
            minute_num = int(s[4:], 2)
            if (hour_num < 12) and (minute_num < 60):
                res.append('{0}:{1:02}'.format(hour_num, minute_num))

        return res

    def readBinaryWatch2(self, num):
        return ['{0}:{1:02}'.format(h, m) for h in range(12) for m in range(60) if (bin(h) + bin(m)).count('1') == num]


if __name__ == "__main__":
    sol = Solution()
    for num in range(9):
        # print(sol.readBinaryWatch1(num))
        print(sol.readBinaryWatch2(num))
