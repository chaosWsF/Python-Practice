r"""
Given a non-empty special binary tree consisting of nodes with the non-negative value, where 
each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then 
this node's value is the smaller value among its two sub-nodes. More formally, the property 
root.val = min(root.left.val, root.right.val) always holds. Given such a binary tree, you need 
to output the second minimum value in the set made of all the nodes' value in the whole tree. 
If no such second minimum value exists, output -1 instead.

Example 1:

    Input:

        2
       / \
      2   5
         / \
        5   7

    Output: 5
    Explanation: The smallest value is 2, the second smallest value is 5.

Example 2:

    Input:

        2
       / \
      2   2

    Output: -1
    Explanation: The smallest value is 2, but there isn't any second smallest value.

"""


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root):
        left, right = root.left, root.right
        if not (left and right):
            return -1
        elif left.val == right.val:
            res_l = self.findSecondMinimumValue(left)
            res_r = self.findSecondMinimumValue(right)
            if -1 in [res_l, res_r]:
                return max(res_l, res_r)
            else:
                return min(res_l, res_r)
        elif left.val < right.val:
            res_l = self.findSecondMinimumValue(left)
            if res_l == -1:
                return right.val
            else:
                return min(right.val, res_l)
        else:
            res_r = self.findSecondMinimumValue(right)
            if res_r == -1:
                return left.val
            else:
                return min(left.val, res_r)
