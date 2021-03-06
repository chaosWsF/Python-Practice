"""
In a town, there are N people labelled from 1 to N. There is a 
rumor that one of these people is secretly the town judge.

If the town judge exists, then:

    The town judge trusts nobody
    Everybody (except for the town judge) trusts the town judge
    There is exactly one person that satisfies properties 1 and 2

You are given trust, an array of pairs trust[i] = [a, b] 
representing that the person labelled a trusts the person 
labelled b.

If the town judge exists and can be identified, return the label 
of the town judge. Otherwise, return -1.

Example 1:

    Input: N = 2, trust = [[1,2]]
    Output: 2

Example 2:

    Input: N = 3, trust = [[1,3],[2,3]]
    Output: 3

Example 3:

    Input: N = 3, trust = [[1,3],[2,3],[3,1]]
    Output: -1

Example 4:

    Input: N = 3, trust = [[1,2],[2,3]]
    Output: -1

Example 5:

    Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
    Output: 3

Note:

    1 <= N <= 1000
    trust.length <= 10000
    trust[i] are all different
    trust[i][0] != trust[i][1]
    1 <= trust[i][0], trust[i][1] <= N
"""


class Solution:
    def findJudge(self, N, trust):
        """direct modelling a graph"""
        vertex = set(range(1, N + 1))
        edge_out = []
        edge_in = []
        for vo, vi in trust:
            edge_out.append(vo)
            edge_in.append(vi)
        edge_zero_outdegree = vertex.difference(edge_out)
        
        if len(edge_zero_outdegree) == 1:
            town_judge = edge_zero_outdegree.pop()
        else:
            return -1
        
        if edge_in.count(town_judge) == N - 1:
            return town_judge
        else:
            return -1
    
    def findJudge2(self, N, trust):
        """calculate deg_diff = in_deg - out_dig"""
        deg_diff = [0] * N
        for vertex_out, vertex_in in trust:
            deg_diff[vertex_out - 1] -= 1
            deg_diff[vertex_in - 1] += 1

        for i in range(N):
            if deg_diff[i] == N - 1:
                return i + 1
        
        return -1

    def findJudge3(self, N, trust):
        """calculate indegree firstly by adjacency matrix"""
        non_judge = {}
        adj_mat = [[] for _ in range(N + 1)]
        # [[]] * (N + 1) is wrong because []s comes from 
        # the same reference, list.append() will change all.

        for edge_0, edge_1 in trust:
            non_judge[edge_0] = 0
            adj_mat[edge_1].append(edge_0)
        
        for i in range(1, N + 1):
            if (len(adj_mat[i]) == N - 1) and (i not in non_judge):
                return i

        return -1
