"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

        3
       / \\
      9  20
        /  \\
       15   7

return its depth = 3.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Iteratively
        max_depth = 0
        
        stack = []
        path_depth = 0
        while root or stack:
            if root:
                path_depth += 1
                stack.append((root,path_depth))
                root = root.left
            else:
                root, path_depth = stack.pop()
                root = root.right
                max_depth = max(max_depth, path_depth)
        
        return max_depth
    
    def maxDepth1(self, root: Optional[TreeNode]) -> int:
        # Recursively
        if not root:
            return 0
        else:
            return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth2(self, root):
        """DFS"""
        if not root:
            return 0
        
        tr_l = root.left
        tr_r = root.right
        max_depth = 1
        if (not tr_l) and (not tr_r):
            return max_depth
        elif tr_l and (not tr_r):
            max_depth += self.maxDepth(tr_l)
        elif (not tr_l) and tr_r:
            max_depth += self.maxDepth(tr_r)
        else:
            max_depth += max(self.maxDepth(tr_l), self.maxDepth(tr_r))
        
        return max_depth
