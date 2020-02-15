"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path
from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """DFS"""
        if not root:
            return 0
        
        tr_l = root.left
        tr_r = root.right
        min_depth = 1
        if (not tr_l) and (not tr_r):
            return min_depth
        elif tr_l and (not tr_r):
            min_depth += self.minDepth(tr_l)
        elif (not tr_l) and tr_r:
            min_depth += self.minDepth(tr_r)
        else:
            min_depth += min(self.minDepth(tr_l), self.minDepth(tr_r))
        
        return min_depth

    def minDepth2(self, root):
        """BFS"""
        if not root:
            return 0
        
        min_depth = 1
        cur_level = [root.left, root.right]
        while any(cur_level):
            next_level = []
            for cur in cur_level:
                if cur:
                    cur_left = cur.left
                    cur_right = cur.right
                    if (not cur_left) and (not cur_right):
                        return min_depth + 1
                    else:
                        next_level += [cur_left, cur_right]
            
            min_depth += 1
            cur_level = next_level
        
        return min_depth
