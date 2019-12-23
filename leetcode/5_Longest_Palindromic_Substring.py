class Solution:
    def longestPalindrome(self, s):
        
        n = len(s)
        # TODO: change to bisection
        for i in range(n, 0, -1):
            for j in range(0, n - i + 1):
                s_ij = s[j:j+i]
                if s_ij == s_ij[::-1]:
                    return s_ij


if __name__ == "__main__":

    input = 'babad'
    # input = 'cbbd'
    # input = 'cbd'

    sol = Solution()
    print(sol.longestPalindrome(input))