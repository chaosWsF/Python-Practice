r"""
Given a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of 
the tree, and every node has no left child and only 1 right child.

Example 1:

    Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

         5
        / \
      3    6
     / \    \
    2   4    8
   /        / \ 
  1        7   9

    Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

    1
     \
      2
       \
        3
         \
          4
           \
            5
             \
              6
               \
                7
                 \
                  8
                   \
                    9  

Constraints:
    1. The number of nodes in the given tree will be between 1 and 100.
    2. Each node will have a unique integer value from 0 to 1000.
"""


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST1(self, root):
        nodes = []
        def dfs(tree):
            if tree:
                dfs(tree.left)
                nodes.append(tree.val)
                dfs(tree.right)

        dfs(root)

        res = cur = TreeNode()
        for x in nodes:
            cur.right = TreeNode(x)
            cur = cur.right
        
        return res.right

        # nodes = []
        # def dfs(tree):
        #     if tree:
        #         dfs(tree.right)
        #         nodes.append(tree.val)
        #         dfs(tree.left)
        # 
        # dfs(root)
        # 
        # res = TreeNode(val=nodes[0])
        # for i in range(1, len(nodes)):
        #     res = TreeNode(val=nodes[i], right=res)
        # 
        # return res


    def increasingBST2(self, root):
        """Python 3's yield from"""
        def dfs(tree):
            if tree:
                yield from dfs(tree.left)
                yield tree.val
                yield from dfs(tree.right)
        
        res = cur = TreeNode()
        for x in dfs(root):
            cur.right = TreeNode(x)
            cur = cur.right
        
        return res.right

    def increasingBST3(self, root):
        def dfs(tree):
            if tree:
                dfs(tree.left)
                tree.left = None
                self.cur.right = tree
                self.cur = tree
                dfs(tree.right)

        res = self.cur = TreeNode()
        dfs(root)
        return res.right
