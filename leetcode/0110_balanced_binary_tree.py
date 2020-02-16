"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

  a binary tree in which the left and right subtrees of every 
  node differ in height by no more than 1.

Example 1:

  Given the following tree [3,9,20,null,null,15,7]:

    3
   / \\
  9  20
    /  \\
   15   7

  Return true.

Example 2:

  Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \\
     2   2
    / \\
   3   3
  / \\
 4   4

  Return false.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """DFS"""
        if not root:
            return True
        
        tr_l = root.left
        tr_r = root.right
        if (not tr_l) and (not tr_r):
            return True
        elif tr_l and (not tr_r):
            return not (tr_l.left or tr_l.right)
        elif (not tr_l) and tr_r:
            return not (tr_r.left or tr_r.right)
        else:
            pass
