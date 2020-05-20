r"""
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of 
the original BST is changed to the original key plus sum of all keys greater than the 
original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13

Note: This question is the same as 1038 -->
      https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def __init__(self):
        self.cumsum = 0
    
    def convertBST(self, root):
        if root:
            self.convertBST(root.right)
            self.cumsum += root.val
            root.val = self.cumsum
            self.convertBST(root.left)
        
        return root
