r"""
Given a binary tree and a sum, determine if the tree has a 
root-to-leaf path such that adding up all the values along the 
path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which
sum is 22.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """DFS"""
        if not root:
            return False
        
        if (not root.left) and (not root.right):
            return root.val == sum
        else:
            return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

    def hasPathSum2(self, root, sum):
        """BFS"""
        if not root:
            return False
        
        cur_level = [root]
        cur_sums = [sum]
        while cur_level:
            next_level = []
            next_sums = []
            for node, cur_sum in zip(cur_level, cur_sums):
                if not (node.left or node.right):
                    if cur_sum == node.val:
                        return True
                    else:
                        continue

                if node.left:
                    next_level.append(node.left)
                    next_sums.append(cur_sum - node.val)
                
                if node.right:
                    next_level.append(node.right)
                    next_sums.append(cur_sum - node.val)
            
            cur_level = next_level
            cur_sums = next_sums

        return False
