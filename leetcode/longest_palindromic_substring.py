class Solution:
    def longestPalindrome(self, s):
        
        # n = len(s)
        # if s == s[::-1]:
        #     result = s
        # else:
        #     result = s[0]
        
        # p = (n + 1) / 2
        # i = int(p)
        # while (1 < p < n) and (len(result) <= i):
        #     j = 0
        #     while j <= n - i:
        #         s_ij = s[j:j+i]
        #         if s_ij == s_ij[::-1]:
        #             result = s_ij
        #             p = (n + p) / 2
        #             i = int(p)
        #             break
                
        #         if j == n - i:
        #             p = (p + 1) / 2
        #             i = int(p)
        #             break

        #         j += 1
        
        # return result

        n = len(s)
        if n > 0:
            for i in range(n, 0, -1):
                for j in range(0, n - i + 1):
                    s_ij = s[j:j+i]
                    if s_ij == s_ij[::-1]:
                        return s_ij
        else:
            return s
