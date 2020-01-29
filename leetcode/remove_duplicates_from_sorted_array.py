"""
Given a sorted array nums, remove the duplicates in-place such 
that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this 
by modifying the input array in-place with O(1) extra memory.

Example 1:

    Given nums = [1,1,2],

    Your function should return length = 2, with the first two 
    elements of nums being 1 and 2 respectively.

    It doesn't matter what you leave beyond the returned length.

Example 2:

    Given nums = [0,0,1,1,1,2,2,3,3,4],

    Your function should return length = 5, with the first five 
    elements of nums being modified to 0, 1, 2, 3, and 4 
    respectively.

    It doesn't matter what values are set beyond the returned 
    length.

Clarification:

Confused why the returned value is an integer but your answer 
is an array?

Note that the input array is passed in by reference, which 
means modification to the input array will be known to the 
caller as well.

Internally you can think of this:

    // nums is passed in by reference. 
    (i.e., without making a copy)
    int len = removeDuplicates(nums);

    // any modification to nums in your function would be 
    known by the caller.
    // using the length returned by your function, it prints 
    the first len elements.
    for (int i = 0; i < len; i++) {
        print(nums[i]);
    }
"""

class Solution:
    def removeDuplicates(self, nums):
        """unique (ordered), assign"""
        if not nums:
            return 0

        tmp = list(dict.fromkeys(nums))
        nums[:len(tmp)] = tmp
        nums[len(tmp):] = []
        
        return len(nums)

    def removeDuplicates2(self, nums):
        """unique (unordered), assign"""
        if not nums:
            return 0

        tmp = set(nums)
        nums[:len(tmp)] = sorted(list(tmp))
        nums[len(tmp):] = []
        
        return len(nums)

    def removeDuplicates3(self, nums):
        """remove one by one"""
        if not nums:
            return 0

        queue = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] == queue:
                # del nums[i]
                nums[i:i+1] = []
            else:
                queue = nums[i]
                i += 1
        
        return len(nums)

    def removeDuplicates4(self, nums):
        """pop/append (slower)"""
        if not nums:
            return 0

        for _ in range(len(nums)):
            tmp = nums.pop(0)
            if not nums:
                nums.append(tmp)

            if tmp != nums[-1]:
                nums.append(tmp)

        return len(nums)

    def removeDuplicates5(self, nums):
        """count/remove (very slow)"""
        if not nums:
            return 0
        
        if nums[0] == nums[-1]:
            return 1
        elif nums[0] < nums[-1]:
            step_size = 1
        else:
            step_size = -1
        
        for n in range(nums[0], nums[-1] + step_size, step_size):
            while nums.count(n) > 1:
                nums.remove(n)

        return len(nums)

    def removeDuplicates6(self, nums):
        """brutal solution, remove block by block (slower)"""
        if not nums:
            return 0

        queue = nums[0]
        i = 1
        while i < len(nums):
            j = 0
            while i + j < len(nums):
                if nums[i + j] == queue:
                    j += 1
                else:
                    queue = nums[i + j]
                    break
            
            if j > 0:
                # del nums[i:i+j]
                nums[i:i+j] = []
            i += 1

        return len(nums)
