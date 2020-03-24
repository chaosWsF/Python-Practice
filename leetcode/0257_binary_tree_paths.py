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
            return 
        
        result = []
        stack = [root]
        paths = [str(root.val)]
        while stack:
            cur = stack.pop()
            cur_path = paths.pop()
            cur_left = cur.left
            cur_right = cur.right
            if not (cur_right or cur_left):
                result.append(cur_path)
            else:
                if cur_right:
                    stack.append(cur_right)
                    paths.append(cur_path + '->' + str(cur.right.val))

                if cur_left:
                    stack.append(cur_left)
                    paths.append(cur_path + '->' + str(cur.left.val))

        return result

    def binaryTreePaths2(self, root):
        """Recursion"""
        if not root:
            return []
        
        return self.get_path(root, [])
    
    def get_path(self, root, paths):
        
        if not (root.left or root.right):
            return ['->'.join(paths + [str(root.val)])]
        else:
            paths.append(str(root.val))
            left_path = []
            right_path = []
            if root.left:
                left_path = self.get_path(root.left, paths)
            
            if root.right:
                right_path = self.get_path(root.right, paths)

            paths.pop()
            return left_path + right_path