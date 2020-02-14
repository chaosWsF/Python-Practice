"""
Given a binary tree, return the bottom-up level order traversal of
its nodes' values. (ie, from left to right, level by level from leaf
to root).

For example:

Given binary tree [3,9,20,null,null,15,7],

     3
    / \\
   9   20
      /  \\
     15   7

return its bottom-up level order traversal as:

    [
      [15,7],
      [9,20],
      [3]
    ]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        """BFS"""
        if not root:
            return None
        
        levels = [[root.val]]
        cur_level = [root.left, root.right]
        while True:
            level_val = []
            next_level = []
            n_null = 0
            for node in cur_level:
                if node:
                    level_val.append(node.val)
                    next_level += [node.left, node.right]
                else:
                    n_null += 1
            
            if n_null < len(cur_level):
                levels.append(level_val)
                # levels = [level_val] + levels
                cur_level = next_level
            else:
                break
        
        return levels[::-1]
        # return levels
