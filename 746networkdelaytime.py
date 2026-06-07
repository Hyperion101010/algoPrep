class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        """
            Implementation using Djikstra's algorithm.
        """
        self.pq = []

        self.graph = {}

        for each_vertex in times:
            if each_vertex[0] not in self.graph:
                self.graph[each_vertex[0]] = [(each_vertex[1], each_vertex[2])]
            else:
                self.graph[each_vertex[0]].append((each_vertex[1], each_vertex[2]))

        dist = [1e9 for i in range(n+1)]

        dist[k] = 0

        self.pq.append((0, k))
        heapify(self.pq)

        while len(self.pq) > 0:
            wgt, node = heappop(self.pq)

            # If indirectly we have a weight thats smaller than its real weight then continue
            if dist[node] < wgt:
                continue

            if node not in self.graph:
                continue

            for each_neighbour in self.graph[node]:
                each_neighbour_node, each_wgt = each_neighbour
                if dist[each_neighbour_node] > dist[node] + each_wgt:
                    dist[each_neighbour_node] = dist[node] + each_wgt
                    heappush(self.pq, (dist[each_neighbour_node], each_neighbour_node))
        
        mx = -1

        for each_node in range(1, n+1):
            if mx < dist[each_node]:
                mx = dist[each_node]
        
        if mx == 1e9:
            return -1
        
        return mx
