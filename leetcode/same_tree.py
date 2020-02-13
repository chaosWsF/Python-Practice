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
        """DFS"""
        if (not p) ^ (not q):
            return False
        elif not (p or q):
            return True
        elif p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False


def lst2tree(l):
    """Convert list into Tree (BFS)"""
    if (not l) or (l[0] == 'null'):
        return None
    
    tree = TreeNode(l[0])

    i = 1
    n_nodes = 2
    cur_level = [tree]
    while i < len(l):
        nodes = []
        n_null = 0
        for nn in range(n_nodes):
            if i + nn < len(l):
                node = l[i + nn]
                if (not node) or (node == 'null'):
                    n_null += 1
                    nodes.append(None)
                else:
                    nodes.append(node)
            else:
                n_null += 1
                nodes.append(None)

        j = 0
        next_level = []
        for cur in cur_level:
            if cur:
                if nodes[j]:
                    cur.left = TreeNode(nodes[j])
                
                if nodes[j + 1]:
                    cur.right = TreeNode(nodes[j + 1])
                
                next_level += [cur.left, cur.right]
                j += 2

        i += n_nodes
        n_nodes = 2 * (n_nodes - n_null)
        cur_level = next_level

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
