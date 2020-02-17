"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

  a binary tree in which the left and right subtrees of every 
  node differ in height by no more than 1.

Example 1:

  Given the following tree [3,9,20,null,null,15,7]:

    3
   / \\
  9  20
    /  \\
   15   7

  Return true.

Example 2:

  Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \\
     2   2
    / \\
   3   3
  / \\
 4   4

  Return false.
"""


class Solution:    
    def isBalanced(self, root):
        """DFS (recursive)"""
        if not root:
            return True
        
        def helper(tree):
            if not tree:
                return 0
            
            h_l = helper(tree.left)
            h_r = helper(tree.right)
            if (h_l == -1) or (h_r == -1) or (abs(h_l - h_r) > 1):
                return -1

            return max(h_l, h_r) + 1
        
        return helper(root) >= 0
    
    def isBalanced2(self, root):
        """DFS (iteration)"""
        if not root:
            return True
        
        stack = [root]
        depth = {None: 0}
        while stack:
            tree = stack[-1]
            tr_l = tree.left
            tr_r = tree.right          
            if tr_l and (tr_l not in depth):
                stack.append(tr_l)
            elif tr_r and (tr_r not in depth):
                stack.append(tr_r)
            else:            
                if not (tr_l or tr_r):
                    depth[tree] = 1
                else:
                    if abs(depth[tr_l] - depth[tr_r]) > 1:
                        return False
                    depth[tree] = max(depth[tr_l], depth[tr_r]) + 1
                stack.pop()
        
        return True
