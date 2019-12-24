import time
from longest_palindromic_substring import Solution

if __name__ == "__main__":

    # input = 'babad'
    # input = 'cbbd'
    input = 'abacab'
    # input = 'abcda'
    # input = 'adam'

    sol = Solution()
    t0 = time.perf_counter()
    print(sol.longestPalindrome(input))
    print(time.perf_counter() - t0)
