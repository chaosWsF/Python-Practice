class Solution:
    def largestSumAfterKNegations(self, A, K):

        A = sorted(A)
        
        try:
            if A[K-1] < 0:  # K <= num(A<0)
                return sum(A) - 2 * sum(A[:K])
        except IndexError:  # K > len(A)
            pass

        for i, a in enumerate(A):
            if a < 0:
                A[i] = -a
            else:
                break

        return sum(A) - ((K-i) % 2) * 2 * min(A)
