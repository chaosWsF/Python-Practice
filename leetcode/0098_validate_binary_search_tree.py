"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

  Input: [2,1,3]
  Output: true

Example 2:

    5
   / \
  1   4
     / \
    3   6

  Input: [5,1,4,null,null,3,6]
  Output: false
  Explanation: The root node's value is 5 but its right child's value is 4.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """DFS (recursive)"""
        def helper(tree, lower=float('-inf'), upper=float('inf')):
            if not tree:
                return True
            
            val = tree.val
            if (val <= lower) or (val >= upper):
                return False
            
            return helper(tree.left, lower, val) and helper(tree.right, val, upper)
        
        return helper(root)

    def isValidBST2(self, root):
        """DFS (Iteration)"""
        if not root:
            return True
        
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            tree, lower, upper = stack.pop()
            if tree:
                if (tree.val <= lower) or (tree.val >= upper):
                    return False
                
                stack.append((tree.left, lower, tree.val))
                stack.append((tree.right, tree.val, upper))

        return True
