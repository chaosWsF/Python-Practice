r"""
Invert a binary tree.
Example:
Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """Recursive"""
        if not root:
            return root
        
        left = self.invertTree(root.right)
        right = self.invertTree(root.left)
        root.left = left
        root.right = right
        return root

    def invertTree2(self, root):
        """Iterative (DFS)"""
        stack = []
        cur = root
        while cur:
            stack.append(cur)
            cur = cur.left
        
        while stack:
            tree = stack.pop()
            # tree_r = tree.right
            # while tree_r:
            #     stack.append(tree_r)
            #     tree_r = tree_r.left
            
            tmp = tree.left
            tree.left = tree.right
            tree.right = tmp
        
        return root
