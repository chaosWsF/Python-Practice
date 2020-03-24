r"""
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """Iteration"""
        if not root:
            return []
        
        stack = [root]
        paths = deque([str(root.val)])
        while stack:
            cur = stack.pop()
            cur_path = paths.pop()
            cur_left = cur.left
            cur_right = cur.right
            if not (cur_right or cur_left):
                paths.appendleft(cur_path)
            else:
                if cur_right:
                    stack.append(cur_right)
                    paths.append(cur_path + '->' + str(cur.right.val))

                if cur_left:
                    stack.append(cur_left)
                    paths.append(cur_path + '->' + str(cur.left.val))

        return paths

    def binaryTreePaths2(self, root):
        """Recursion"""        
        return self.get_paths(root, []) if root else []
    
    def get_paths(self, root, paths):
        if not (root.left or root.right):
            return ['->'.join(paths + [str(root.val)])]
        else:
            paths.append(str(root.val))
            new_paths = []
            if root.left:
                new_paths += self.get_paths(root.left, paths)
            
            if root.right:
                new_paths += self.get_paths(root.right, paths)

            paths.pop()
            return new_paths
