r"""
Given a Binary Search Tree and a target number, return true if there exist two elements in the 
BST such that their sum is equal to the given target.

Example 1:

    Input:

        5
       / \
      3   6
     / \   \
    2   4   7

    Target = 9

    Output: True

Example 2:

    Input:

        5
       / \
      3   6
     / \   \
    2   4   7

    Target = 28

    Output: False

"""


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget1(self, root, k):    # 96ms
        def helper(node, lst = []):
            if node:
                helper(node.left)
                lst.append(node.val)
                helper(node.right)
            
            return lst

        vals = helper(root)

        i, j = 0, len(vals) - 1
        while i < j:
            if vals[i] + vals[j] > k:
                j -= 1
            elif vals[i] + vals[j] == k:
                return True
            else:
                i += 1
        
        return False
    
    def findTarget2(self, root, k):    # 72ms
        if not root:    return False
        d = set()
        stack = [root]
        while stack:
            node = stack.pop()
            tmp = node.val
            if tmp in d:    return True
            d.add(k - tmp)
            if node.left:    stack.append(node.left)
            if node.right:    stack.append(node.right)
        
        return False
