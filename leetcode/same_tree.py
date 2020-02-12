"""
Given two binary trees, write a function to check if they are the
same or not.

Two binary trees are considered the same if they are structurally
identical and the nodes have the same value.

Example 1:

    Input:     1         1
              / \\      / \\
             2   3     2   3

            [1,2,3],   [1,2,3]

    Output: true

Example 2:

    Input:     1         1
              /           \\
             2             2

            [1,2],     [1,null,2]

    Output: false

Example 3:

    Input:     1         1
              / \\      / \\
             2   1     1   2

            [1,2,1],   [1,1,2]

    Output: false
"""


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        """DFS (20ms)"""
        if (not p) ^ (not q):
            return False
        elif not (p or q):
            return True

        single_node_1 = not (p.left or p.right)
        single_node_2 = not (q.left or q.right)
        if single_node_1 ^ single_node_2:
            return False
        elif single_node_1 and single_node_2:
            return p.val == q.val

        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False



def lst2tree(l):
    """Convert list into Tree (BFS)"""
    if (not l) or (l[0] == 'null'):
        return TreeNode('null')
    
    tree = TreeNode(l[0])

    i = 1
    num_nodes = 2
    last_level = [tree]
    while i < len(l):
        if i + num_nodes > len(l):
            l += ['null'] * (i + num_nodes - len(l))
        
        level_nodes = l[i:i+num_nodes]
        j = 0
        cur_level = []
        for cur in last_level:
            if cur.val != 'null':
                cur.left = TreeNode(level_nodes[j])
                cur.right = TreeNode(level_nodes[j+1])
                cur_level += [cur.left, cur.right]
                j += 2
        
        i += num_nodes
        num_nodes = 2 * (num_nodes - level_nodes.count('null'))
        last_level = cur_level

    return tree


if __name__ == "__main__":
    # try_tree_val = [1, 2, 'null', 4, 5, 'null', 7]
    # try_tree = lst2tree(try_tree_val)

    input_1 = [1, 2, 3]
    input_2 = [1, 2, 3]

    input_tree_1 = lst2tree(input_1)
    input_tree_2 = lst2tree(input_2)

    sol = Solution()
    print(sol.isSameTree(input_tree_1, input_tree_2))
