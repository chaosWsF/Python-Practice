"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two 
nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be 
a descendant of itself).”

Example 1:

    Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
    Output: 6
    Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:

    Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
    Output: 2
    Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself 
    according to the LCA definition.

Note:
    All of the nodes' values will be unique.
    p and q are different and both values will exist in the BST.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # NOTE: it is a binary search tree
    def lowestCommonAncestor(self, root, p, q):
        """76ms"""
        if (p.val < root.val) and (q.val < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (p.val > root.val) and (q.val > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

    def lowestCommonAncestor2(self, root, p, q):
        """64ms"""
        p_val = p.val
        q_val = q.val
        while root:
            root_val = root.val
            if (p_val < root_val) and (q_val < root_val):
                root = root.left
            elif (p_val > root_val) and (q_val > root_val):
                root = root.right
            else:
                return root
