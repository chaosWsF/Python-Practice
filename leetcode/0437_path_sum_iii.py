r"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict


class Solution:
    def pathSum1(self, root, sum):
        if not root:
            return 0
        
        stack = [(root, [sum - root.val])]
        res = 0
        while stack:
            node, cur_rem = stack.pop()
            node_l = node.left
            node_r = node.right
            for r in cur_rem:
                if r == 0:
                    res += 1
            
            if node_l:
                val = node_l.val
                next_rem = [x - val for x in cur_rem]                
                next_rem.append(sum - val)
                stack.append((node_l, next_rem))
            
            if node_r:
                val = node_r.val
                next_rem = [x - val for x in cur_rem]
                next_rem.append(sum - val)
                stack.append((node_r, next_rem))
        
        return res
    
    def dfs(self, node, cum_sum, path_sum):
        cum_sum += node.val
        self.res += self.d[cum_sum - path_sum]
        self.d[cum_sum] += 1
        
        if node.left:
            self.dfs(node.left, cum_sum, path_sum)
        
        if node.right:
            self.dfs(node.right, cum_sum, path_sum)
        
        self.d[cum_sum] -= 1
    
    def pathSum2(self, root, path_sum):
        if not root:
            return 0
        
        self.d = defaultdict(int)
        self.d[0] = 1
        self.res = 0
        cum_sum = 0
        self.dfs(root, cum_sum, path_sum)
        return self.res
