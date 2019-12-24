class Solution:
    def preimageSizeFZF(self, K):
        K = K + 1
        s = [6]
        while s[-1] <= K:
            s.append(s[-1] * 5 + 1)

        s.pop()

        while K > 6:
            K = K % s[-1]
            s.pop()
        
        K = K % 6
        if K == 0:
            return 0
        else:
            return 5
