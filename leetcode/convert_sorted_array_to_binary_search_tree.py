"""
Given an array where elements are sorted in ascending order, 
convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a 
binary tree in which the depth of the two subtrees of every node
never differ by more than 1.

Example:

    Given the sorted array: [-10,-3,0,5,9],

    One possible answer is: [0,-3,9,-10,null,5], which represents
    the following height balanced BST:

        0
       / \\
     -3   9
     /   /
   -10  5
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """DFS"""
        if not nums:
            return None
        
        n = len(nums)
        if n == 1:
            return TreeNode(nums[0])
        
        mid = n // 2
        tree = TreeNode(nums[mid])
        if n == 2:
            tree.left = TreeNode(nums[mid-1])
        else:
            tree.left = self.sortedArrayToBST(nums[:mid])
            tree.right = self.sortedArrayToBST(nums[mid + 1:])

        return tree
