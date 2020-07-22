"""
Consider all the leaves of a binary tree. From left to right order, the values of those leaves form a leaf value sequence.

    https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/16/tree.png

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8). Two binary trees are considered leaf-similar 
if their leaf value sequence is the same. Return true if and only if the two given trees with head nodes root1 and root2 are 
leaf-similar. 

Constraints:
    1. Both of the given trees will have between 1 and 200 nodes.
    2. Both of the given trees will have values between 0 and 200
"""


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar1(self, root1, root2):
        def leafseq(node, leaves):
            if node:
                if not (node.left or node.right):
                    leaves.append(node.val)
                else:
                    leafseq(node.left, leaves)
                    leafseq(node.right, leaves)
            
            return leaves

        return leafseq(root1, []) == leafseq(root2, [])

    def leafSimilar2(self, root1, root2):
        """Python 3's yield from"""
        def leafseq(node):
            if node:
                if not (node.left or node.right):
                    yield node.val
                else:
                    yield from leafseq(node.left)
                    yield from leafseq(node.right)
            
        return list(leafseq(root1)) == list(leafseq(root2))
