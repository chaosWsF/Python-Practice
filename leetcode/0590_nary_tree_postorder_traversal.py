"""
Given an n-ary tree, return the postorder traversal of its nodes' values. Nary-Tree input serialization 
is represented in their level order traversal, each group of children is separated by the null value 
(See examples). 

Follow up: Recursive solution is trivial, could you do it iteratively?

Example 1:

    https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png

    Input: root = [1,null,3,2,4,null,5,6]
    Output: [5,6,3,2,4,1]

Example 2:

    https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png

    Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
    Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]

Constraints:
    The height of the n-ary tree is less than or equal to 1000
    The total number of nodes is between [0, 10^4]
"""


# class Node:
#     """Definition for a Node."""
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children


class Solution:
    def __init__(self):
        self.post_lst = []
    
    def postorder(self, root):
        """recursion"""
        if root:
            for leaf in root.children:
                self.postorder(leaf)
            
            self.post_lst.append(root.val)
        
        return self.post_lst

    def postorder2(self, root):
        """iteration"""
        if not root:
            return []
        
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend(node.children)
        
        return res[::-1]
