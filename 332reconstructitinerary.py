class Solution:
    def traverse(self, startNode: str):

        # 1. We check all neighbours of startNode.
        # 2. We traverse one by one and ensure we can come back.
        # 3. Those we cannot come back we have to traverse them first in alhpbetical order.
        # 4. Then traverse those where we can come back in alphabetical order.

        # Correct solution
        # 1. Do dfs of all the outgoing edges.
        # 2. When dfs is done then remove the outgoing edge.
        # 3. To preserve lexographically we need to ssort it in descending order.

        # Now each element of the grapg adj list is a sorted node.
        # So lets process those with out going edges.

        # Considering smaller elements first.

        # Solutions link - https://leetcode.com/problems/reconstruct-itinerary/solutions/8400071/hierholzers-algorithm-eulerian-path-in-o-sm7e/

        """
            Key difference between Eulerian path and normal DFS is:
            1. In DFS we visit each node(vertices) only once. Even if nodes have many edges we will skip visiting those edges if the destination 
            node is already visited.
            2. Much different than the normal DFS in the Eulerian paths we visit all the edges such that we can walk back to the destination.
            So we use every edge exactly once. The condition of the problem is also to use all the tickets that are provided.
        """

        if startNode not in self.graph:
            self.lst.append(startNode)
            return

        while len(self.graph[startNode]) > 0:
            # Popping the graph gives us the smallest lexographically outgoing edge.
            ele = self.graph[startNode].popleft()
            self.traverse(ele)
        
        # Post order DFS
        # Heirholze's algorithm to get the euclidean path/cycle.
        self.lst.append(startNode)

        

    def add_edge(self, a, b):
        if a in self.graph:
            self.graph[a].append(b)
        else:
            self.graph[a] = deque([b])


    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # I will do a BFS, where I put those neighbours who are lexogrphically first.
        # Go first in the queue.
        # After putting them in the queue, I also delete that edge so that it doesn't come back.

        self.lst = []

        self.graph = {}

        for each_ticket in tickets:
            from_loc = each_ticket[0]
            to_loc = each_ticket[1]

            self.add_edge(from_loc, to_loc)
        
        for each_key in self.graph.keys():
            self.graph[each_key] = deque(sorted(self.graph[each_key]))

        self.traverse("JFK")

        self.lst = self.lst[::-1]

        return self.lst
