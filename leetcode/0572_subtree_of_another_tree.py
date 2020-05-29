r"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and 
node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this 
node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:

Given tree s:

     3
    / \
   4   5
  / \
 1   2

Given tree t:

   4 
  / \
 1   2

Return true, because t has the same structure and node values with a subtree of s.

Example 2:

Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0

Given tree t:

   4
  / \
 1   2

Return false.

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, s, t):    # 248ms
        def helper(a, b):
            if not (a and b):
                return not (a or b)
            elif a.val != b.val:
                return False
            else:
                return helper(a.left, b.left) and helper(a.right, b.right)

        if not s:
            return not t
        elif helper(s, t):
            return True
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSubtree2(self, s, t):    # 64ms
        """f-string in Python 3.6"""
        def encoding(node):
            if node:
                return f'/{node.val}{encoding(node.left)}{encoding(node.right)}'
        
        return encoding(s).find(encoding(t)) != -1
