r"""
Given a binary search tree and the lowest and highest boundaries as L and R, trim the 
tree so that all its elements lies in [L, R] (R >= L). You might need to change the root 
of the tree, so the result should return the new root of the trimmed binary search tree.

Example 1:

    Input: L = 1, R = 2
        1
       / \
      0   2

    Output: 
        1
         \
          2

Example 2:

    Input: L = 1, R = 3
        3
       / \
      0   4
       \
        2
       /
      1

    Output: 
        3
       / 
      2   
     /
    1

"""


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(self, root, L, R):
        if not root:
            return root
        elif root.val > R:
            return self.trimBST(root.left, L, R)
        elif root.val < L:
            return self.trimBST(root.right, L, R)
        else:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
            return root
