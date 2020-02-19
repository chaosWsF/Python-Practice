"""
For a non-negative integer X, the array-form of X is an array of its digits in left to right order.
For example, if X = 1231, then the array form is [1,2,3,1].

Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.

Example 1:

    Input: A = [1,2,0,0], K = 34
    Output: [1,2,3,4]
    Explanation: 1200 + 34 = 1234

Example 2:

    Input: A = [2,7,4], K = 181
    Output: [4,5,5]
    Explanation: 274 + 181 = 455

Example 3:

    Input: A = [2,1,5], K = 806
    Output: [1,0,2,1]
    Explanation: 215 + 806 = 1021

Example 4:

    Input: A = [9,9,9,9,9,9,9,9,9,9], K = 1
    Output: [1,0,0,0,0,0,0,0,0,0,0]
    Explanation: 9999999999 + 1 = 10000000000
 
Note：
    1. 1 <= A.length <= 10000
    2. 0 <= A[i] <= 9
    3. 0 <= K <= 10000
    4. If A.length > 1, then A[0] != 0
"""

class Solution:
    def addToArrayForm1(self, A, K):
        """speed 1st (276 ms)"""
        if K == 0:
            return A
        
        i = len(A) - 1
        carry = 0
        while (K > 0) or (carry == 1):
            if i >= 0:
                A[i] += K % 10 + carry
                if A[i] >= 10:
                    A[i] -= 10
                    carry = 1
                else:
                    carry = 0
                
                i -= 1
            else:
                if carry == 1:
                    K += 1
                    carry = 0
                
                A = [K % 10] + A
            
            K = K // 10
        
        return A
    
    def addToArrayForm2(self, A, K):
        """speed 2nd (304 ms)"""
        return list(str(int(''.join(map(str, A))) + K))

    def addToArrayForm3(self, A, K):
        """speed 3rd (396 ms)"""
        A_str = ''
        for a in A:
            A_str += str(a)
        return list(str(int(A_str) + K))
    
    def addToArrayForm4(self, A, K):
        """speed 4th (408 ms)"""
        A_int = 0
        for a in A:
            A_int = 10 * A_int + a
        return list(str(A_int + K))
    
    def addToArrayForm5(self, A, K):
        """speed 5th (1876 ms)"""
        A_int = 0
        for a in A:
            A_int = 10 * A_int + a
        
        tmp = A_int + K
        if tmp == 0:
            return [0]
        
        result = []
        while tmp > 0:
            result.append(tmp % 10)
            tmp = tmp // 10
        
        return result[::-1]
