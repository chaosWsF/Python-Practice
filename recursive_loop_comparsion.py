from collections import deque
from time import perf_counter


class Solution:
    """
    Leetcode Problem 1: Two Sum
    """
    def twoSum_recursive(self, nums, target):
        """Recursion function with deque"""

        if type(nums) is list:
            self.nums = nums
            dq = deque(sorted(nums))
        else:
            dq = nums

        if dq[0] + dq[-1] == target:
            a_index = self.nums.index(dq[0])
            b_index = self.nums[a_index+1:].index(dq[-1])
            return [a_index, b_index]
        elif dq[0] + dq[-1] > target:
            dq.pop()
            return self.twoSum_recursive(dq, target)
        else:
            dq.popleft()
            return self.twoSum_recursive(dq, target)
    
    def twoSum_loop(self, nums, target):
        """Loop with deque"""

        dq = deque(sorted(nums))
        while dq[0] + dq[-1] != target:
            if dq[0] + dq[-1] > target:
                dq.pop()
            else:
                dq.popleft()
        
        a_index = nums.index(dq[0])
        b_index = nums[a_index+1:].index(dq[-1])
        return [a_index, b_index]


if __name__ == '__main__':

    sol = Solution()
    test_nums = [9, 4, 8, 3, 6, 10, 4, 20, 19]
    test_target = 18

    total_time = 0
    for _ in range(100):
        t0 = perf_counter()
        sol.twoSum_recursive(test_nums, test_target)
        # sol.twoSum_loop(test_nums, test_target)
        total_time += perf_counter() - t0
    
    total_time = (total_time / 100) * 1e6
    print('Recursive used time: {0:.3f} μs'.format(total_time))  # 3.928
    # print('Loop used time: {0:.3f} μs'.format(total_time))  # 2.629
