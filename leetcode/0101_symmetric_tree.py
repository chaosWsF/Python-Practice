"""
Given a binary tree, check whether it is a mirror of itself (ie,
symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \\
  2    2
 / \\ / \\
3   44   3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \\
  2   2
  \\   \\
   3    3
 

Note:
Bonus points if you could solve it both recursively and 
iteratively.
"""


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Iteratively
        stack = [(root.left, root.right)]
        curl, curr = root.left, root.right
        while stack:
            if not curl and not curr:
                curl, curr = stack.pop()
            elif not curl or not curr:
                return False
            elif curl.val != curr.val:
                return False
            else:
                stack.append((curl.right, curr.left))
                curl = curl.left
                curr = curr.right
        
        return True

    def isSymmetric1(self, root):
        """DFS"""
        if not root:
            return True
        
        def helper(tr_l, tr_r):
            if (not tr_l) ^ (not tr_r):
                return False
            elif not (tr_l or tr_r):
                return True
            elif tr_l.val != tr_r.val:
                return False
            else:
                return helper(tr_l.left, tr_r.right) and helper(tr_l.right, tr_r.left)
        
        return helper(root.left, root.right)
    
    def isSymmetric2(self, root):
        """BFS"""
        if not root:
            return True
        
        level = [root.left, root.right]
        n_null = 0
        while n_null < len(level):
            next_level = []
            n_null = 0
            head = 0
            tail = len(level) - 1
            while head < len(level):
                cur = level[head]
                if cur:
                    next_level += [cur.left, cur.right]
                else:
                    n_null += 1
                
                if head < tail:
                    cur_sym = level[tail]
                    if (not cur) ^ (not cur_sym):
                        return False
                    elif not (cur or cur_sym):
                        head += 1
                        tail -= 1
                    elif cur.val == cur_sym.val:
                        head += 1
                        tail -= 1
                    else:
                        return False
                else:
                    head += 1

            level = next_level

        return True


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

    input_1 = [1, 2, 2, 'null', 3, 'null', 3]
    input_tree_1 = lst2tree(input_1)
    sol = Solution()
    print(sol.isSymmetric2(input_tree_1))
