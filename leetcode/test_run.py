from time import perf_counter
from longest_palindromic_substring import Solution

if __name__ == "__main__":

    input = 'babad'
    # input = 'cbbd'
    # input = 'cbd'

    sol = Solution()
    t0 = perf_counter()
    print(sol.longestPalindrome(input))
    print(perf_counter() - t0)
