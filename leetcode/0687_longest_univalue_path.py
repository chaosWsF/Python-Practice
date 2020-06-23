r"""
Given a binary tree, find the length of the longest path where each node in the path has the same value. 
This path may or may not pass through the root. The length of path between two nodes is represented by 
the number of edges between them.

Example 1:

    Input:

                5
               / \
              4   5
             / \   \
            1   1   5

    Output: 2

Example 2:

    Input:

                1
               / \
              4   5
             / \   \
            4   4   5

    Output: 2

Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
"""


class TreeNode:
    """Definition for a binary tree node"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root):
        self.res = 1

        def dfs(node):
            if not node:
                return 0, None
            
            val, left, right = node.val, node.left, node.right
            if not (left or right):
                return 1, val
            
            lres, lval = dfs(left)
            rres, rval = dfs(right)
            if val == lval == rval:
                self.res = max(self.res, 1 + lres + rres)
                return 1 + max(lres, rres), val
            elif val == lval:
                self.res = max(self.res, 1 + lres)
                return 1 + lres, val
            elif val == rval:
                self.res = max(self.res, 1 + rres)
                return 1 + rres, val
            else:
                return 1, val

        dfs(root)
        return self.res - 1
