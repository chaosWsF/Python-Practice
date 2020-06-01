r"""
Given an n-ary tree, return the preorder traversal of its nodes' values. Nary-Tree input serialization 
is represented in their level order traversal, each group of children is separated by the null value 
(See examples). 

Follow up: Recursive solution is trivial, could you do it iteratively? 

Example 1:

    https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png

    Input: root = [1,null,3,2,4,null,5,6]
    Output: [1,3,5,6,2,4]

Example 2:

    https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png

    Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
    Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]

Constraints:
    · The height of the n-ary tree is less than or equal to 1000
    · The total number of nodes is between [0, 10^4]
"""


# class Node:
#     """Definition for a Node."""
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children


class Solution:
    def __init__(self):
        self.res = []
    
    def preorder(self, root):
        """recursion"""
        if root:
            self.res.append(root.val)
            for node in root.children:
                self.preorder(node)
        
        return self.res

    def preorder2(self, root):
        """Iteration"""
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.extend(node.children[::-1])
        
        return res
