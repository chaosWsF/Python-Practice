r"""
You need to construct a string consists of parenthesis and integers from a binary tree with the 
preorder traversing way. The null node needs to be represented by empty parenthesis pair "()". 
And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping 
relationship between the string and the original binary tree.

Example 1:

    Input: Binary tree: [1,2,3,4]

          1
        /   \
       2     3
      /    
     4     

    Output: "1(2(4))(3)"
    Explanation: Originallay it needs to be "1(2(4)())(3()())", but you need to omit all the 
                 unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)".

Example 2:
    Input: Binary tree: [1,2,3,null,4]

          1
        /   \
       2     3
        \  
         4 

    Output: "1(2()(4))(3)"
    Explanation: Almost the same as the first example, except we can't omit the first parenthesis 
                 pair to break the one-to-one mapping relationship between the input and the output.
"""


# class TreeNode:
#     """Definition for a binary tree node."""
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def tree2str1(self, t):    # 48 ms
        if not t:
            return ''
        
        def encoding(node):
            """f format in python 3.6"""
            if node:
                return f'{node.val}({encoding(node.left)})({encoding(node.right)})'
        
        return encoding(t).replace('None', '').replace('()()', '').replace('())', ')').replace(')()', ')')
    
    def tree2str(self, t):    # 44 ms
        if not t:
            return ''
        
        res = str(t.val)
        if t.left:
            res += f'({self.tree2str(t.left)})'
        elif t.right:
            res += '()'
        
        if t.right:
            res += f'({self.tree2str(t.right)})'
        
        return res
