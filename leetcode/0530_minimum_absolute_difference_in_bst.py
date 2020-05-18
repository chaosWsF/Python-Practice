r"""
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

    Input:

       1
        \
         3
        /
       2

    Output: 1
    Explanation: The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).

Note:
    There are at least two nodes in this BST.
    This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def getMinimumDifference(self, root):
        """a general case, 52ms"""
        nodes_val = []
        stack = [root]
        while stack:
            node = stack.pop()
            nodes_val.append(node.val)
            if node.left:
                stack.append(node.left)
            
            if node.right:
                stack.append(node.right)
        
        nodes_val.sort()
        return min(nodes_val[i] - nodes_val[i-1] for i in range(1, len(nodes_val)))

    def getMinimumDifference2(self, root):
        """BST, 48ms"""
        nodes_val = []
        def inorder(node):
            if node:    
                inorder(node.left)
                nodes_val.append(node.val)
                inorder(node.right)
        
        inorder(root)
        return min(nodes_val[i] - nodes_val[i-1] for i in range(1, len(nodes_val)))
