from typing import List

class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))
        self.n = n

    def union(self, a, b):
        pa, pb = self.find(a - 1), self.find(b - 1)
        if pa == pb:
            return False
        self.p[pa] = pb
        self.n -= 1
        return True

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        ufa, ufb = UnionFind(n), UnionFind(n)
        ans = 0
        for t, u, v in edges:
            if t == 3:
                if ufa.union(u, v):
                    ufb.union(u, v)
                else:
                    ans += 1
        ans += sum(
            (t == 1 and not ufa.union(u, v)) or (t == 2 and not ufb.union(u, v))
            for t, u, v in edges
        )
        return ans if ufa.n == 1 and ufb.n == 1 else -1

# Like this sol more:
# class Solution:
#     def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
#         # approach: build out the graph with all the type 3 edges (no cycles)
#         # for subsequent type 1 and 2 edges left, build out the 
#         # the graph until its fully connected
#         # the maximum number of edges we can remove is the number of 
#         # redundant edges during graph building + number of edges left
#         # after completing the graph
#         # cycle detection with disjoint set

#         alice_nodes = [-1] * (n + 1)
#         bob_nodes = [-1] * (n + 1)

#         def helper_find_parent(family, node):
#             if family[node] < 0:
#                 return node
#             family[node] = helper_find_parent(family, family[node])
#             return family[node]

#         num_redundant_edges = 0

#         for typ, u, v in edges:
#             if typ == 3:
#                 # add it to the graph if not redundant
#                 p_u = helper_find_parent(alice_nodes, u)
#                 p_v = helper_find_parent(alice_nodes, v)

#                 if p_u != p_v:
#                     # we can safely join these two subsets
#                     alice_nodes[p_u] += alice_nodes[p_v]
#                     alice_nodes[p_v] = p_u
#                 else:
#                     num_redundant_edges += 1
#         bob_nodes = alice_nodes.copy()
#         # now we build the graph for alice and bob perspectively
#         for typ, u, v in edges:
#             if typ == 1:
#                 # add it to Alice's graph
#                 # add it to the graph if not redundant
#                 p_u = helper_find_parent(alice_nodes, u)
#                 p_v = helper_find_parent(alice_nodes, v)

#                 if p_u != p_v:
#                     # we can safely join these two subsets
#                     alice_nodes[p_u] += alice_nodes[p_v]
#                     alice_nodes[p_v] = p_u
#                 else:
#                     num_redundant_edges += 1

#             if typ == 2:
#                 # add it to Alice's graph
#                 # add it to the graph if not redundant
#                 p_u = helper_find_parent(bob_nodes, u)
#                 p_v = helper_find_parent(bob_nodes, v)

#                 if p_u != p_v:
#                     # we can safely join these two subsets
#                     bob_nodes[p_u] += bob_nodes[p_v]
#                     bob_nodes[p_v] = p_u
#                 else:
#                     num_redundant_edges += 1
#         al = min(alice_nodes)
#         bl = min(bob_nodes)
#         if (al == bl and al == -1 * n):
#             return num_redundant_edges
#         else:
#             return -1