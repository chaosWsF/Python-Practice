"""
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1. Two nodes 
of a binary tree are cousins if they have the same depth, but have different parents. We are given the root 
of a binary tree with unique values, and the values x and y of two different nodes in the tree. Return true 
if and only if the nodes corresponding to the values x and y are cousins. 

Example 1:

    https://assets.leetcode.com/uploads/2019/02/12/q1248-01.png

    Input: root = [1,2,3,4], x = 4, y = 3
    Output: false

Example 2:

    https://assets.leetcode.com/uploads/2019/02/12/q1248-02.png

    Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
    Output: true

Example 3:

    https://assets.leetcode.com/uploads/2019/02/13/q1248-03.png

    Input: root = [1,2,3,null,4], x = 2, y = 3
    Output: false

Constraints:
    1. The number of nodes in the tree will be between 2 and 100.
    2. Each node has a unique integer value from 1 to 100.
"""


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins1(self, root, x, y):
        """BFS, 28ms"""
        selected = set([x, y])
        if root.val in selected:
            return False
        
        prev = [root]
        while prev:
            cur = []
            for node in prev:
                left, right = node.left, node.right
                if left and right and set([left.val, right.val]).issubset(selected):
                    return False
                
                if left:
                    cur.append(left)
                
                if right:
                    cur.append(right)
            
            vals = set([x.val for x in cur])
            if selected.issubset(vals):
                return True
            elif not selected.isdisjoint(vals):
                return False

            prev = cur

        return False
    
    def isCousins2(self, root, x, y):
        """DFS, 32ms"""
        def helper(node, selected, depth, parent):
            if node and node.val == selected:
                return depth, parent
            
            if node:
                return (
                    helper(node.left, selected, depth + 1, node) or 
                    helper(node.right, selected, depth + 1, node)
                )
        
        d_x, p_x = helper(root, x, 0, None)
        d_y, p_y = helper(root, y, 0, None)
        return d_x == d_y and p_x != p_y

    def isCousins3(self, root, x, y):
        """BFS 2, 32ms"""
        stack = [(root, None)]
        while stack:
            x_parent = y_parent = None
            for n, p in stack:
                if n.val == x:
                    x_parent = p
                elif n.val == y:
                    y_parent = p
                
                if x_parent is not None and y_parent is not None:
                    return x_parent != y_parent

            stack = [(func(n), n) for func in (lambda x: x.left, lambda x: x.right) for n, _ in stack if func(n)]
        
        return False
