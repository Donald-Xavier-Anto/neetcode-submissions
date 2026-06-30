"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        st = dict()
        vis = set()
        def construct_graph(nd):
            if nd.val not in st:
                n = Node(nd.val)
                st[nd.val] = n
            else:
                n = st[nd.val]
            vis.add(nd.val)
            for i in nd.neighbors:
                if i.val not in st:
                    nn = Node(i.val)
                    st[i.val] = nn
                else:
                    nn = st[i.val]
                n.neighbors.append(nn)
                if i.val not in vis:
                    construct_graph(i)
            return n
        return construct_graph(node)

            
            


        