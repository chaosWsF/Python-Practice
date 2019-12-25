class Solution:
    def myAtoi(self, str):

        if (not str) or (str in ['-', '+']):
            return 0

        while str[0] == ' ':
            str = str[1:]
            if (not str) or (str in ['-', '+']):
                return 0

        if str[0] == '-':
            sig = -1
            str = str[1:]
        elif str[0] == '+':
            sig = 1
            str = str[1:]
        else:
            sig = 1

        try:
            result = int(str[0])
            for i in range(1, len(str)):
                try:
                    result = int(str[:i+1])
                except ValueError:
                    break
        
        except ValueError:
            return 0
        
        result = sig * result
        if result >= 2**31:
            return 2**31 - 1
        elif result < -2**31:
            return -2**31
        else:
            return result
