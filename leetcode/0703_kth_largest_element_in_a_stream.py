"""
Design a class to find the kth largest element in a stream. Note that it is the kth largest element 
in the sorted order, not the kth distinct element. Your KthLargest class will have a constructor which 
accepts an integer k and an integer array nums, which contains initial elements from the stream. For each 
call to the method KthLargest.add, return the element representing the kth largest element in the stream.

Example:

    int k = 3;
    int[] arr = [4,5,8,2];
    KthLargest kthLargest = new KthLargest(3, arr);
    kthLargest.add(3);   // returns 4
    kthLargest.add(5);   // returns 5
    kthLargest.add(10);  // returns 5
    kthLargest.add(9);   // returns 8
    kthLargest.add(4);   // returns 8

Note: You may assume that nums' length ≥ k-1 and k ≥ 1.
"""

from heapq import heappush, heappop


class KthLargest0:
    """without heapq modules, 428ms"""
    def __init__(self, k, nums):
        self.k = k
        if not nums:
            self.nums = []
        else:
            if len(nums) < k:
                self.nums = sorted(nums)
            else:
                self.nums = sorted(nums)[-k:]
            
            self.res = self.nums[0]

    def add(self, val):
        if not self.nums:
            self.nums.append(val)
            self.res = val
        elif len(self.nums) < self.k or self.res < val:
            self.nums.append(val)
            self.nums.sort()
            if len(self.nums) > self.k and self.res < val:
                self.nums.pop(0)
            
            self.res = self.nums[0]
        
        return self.res


class KthLargest:    # 96ms
    def __init__(self, k, nums):
        self.minHeap = []
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val):
        heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heappop(self.minHeap)

        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
