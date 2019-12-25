class Solution:
    def oddCells(self, n, m, indices):
        
        r = [0] * n
        c = [0] * m
        for ri, ci in indices:
           r[ri] = (r[ri] + 1) % 2
           c[ci] = (c[ci] + 1) % 2

        return sum(r)*m + sum(c)*n - 2*sum(r)*sum(c)
