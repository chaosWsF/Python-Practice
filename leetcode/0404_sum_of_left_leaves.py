r"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):  # 32ms
        if not root:
            return 0
        elif not root.left:
            return self.sumOfLeftLeaves(root.right)
        elif not (root.left.left or root.left.right):
            return root.left.val + self.sumOfLeftLeaves(root.right)
        else:
            return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

    def sumOfLeftLeaves2(self, root):  # 20ms
        if not root:
            return 0
        
        res = 0
        stack = [(root, False)]
        while stack:
            node, is_left = stack.pop()
            node_left = node.left
            node_right = node.right
            if node_left:
                stack.append((node_left, True))
            if node_right:
                stack.append((node_right, False))
            
            res += node.val * (not (node_left or node_right)) * is_left
        
        return res
