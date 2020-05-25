r"""
Given a n-ary tree, find its maximum depth. The maximum depth is the number of nodes along the longest 
path from the root node down to the farthest leaf node. Nary-Tree input serialization is represented in 
their level order traversal, each group of children is separated by the null value (See examples).

Example 1:

    https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png

    Input: root = [1,null,3,2,4,null,5,6]
    Output: 3

Example 2:

    https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png

    Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
    Output: 5

Constraints:
    The depth of the n-ary tree is less than or equal to 1000.
    The total number of nodes is between [0, 10^4].
"""


# # Definition for a Node.
# class Node:
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children


class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        elif not root.children:
            return 1
        else:
            # return 1 + max(map(self.maxDepth, root.children))
            return 1 + max(self.maxDepth(node) for node in root.children)
