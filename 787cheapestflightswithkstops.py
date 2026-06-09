class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Breadth first search from all the neighbours.
        # In this search we will move level by level as per the stops mentioned.
        # For every level we clear our queue and fetch all nodes at that level
        # And for that level we then only insert its next neighbours if its going to reduce height.
        # This inserting in queue if only its smaller helps us avoid the memory limit exceed case cause
        # We don't insert unwanted elements and back edges.
        # If node count > k return 1e9
        # ans = min(of all calls for its all neighbours)

        self.dist = [1e9 for i in range(n+1)]
        self.graph = {}

        for each_item in flights:
            from_node, to_node, price = each_item[0], each_item[1], each_item[2]
            if from_node not in self.graph:
                self.graph[from_node] = [[to_node, price]]
            else:
                self.graph[from_node].append([to_node, price])

        self.k = k
        self.n = n
        self.dst = dst

        ans = self.bfs(src, dst)

        if ans == 1e9:
            return -1
        
        return ans

    
    def bfs(self, src, dest):
        q = deque([])

        self.dist[src] = 0

        q.append((src, 0))

        curr_stop = 0

        # At this point all points till that depth are processed
        while len(q) > 0 and curr_stop < self.k + 1:

            q_sz = len(q)

            while q_sz > 0:
                node, distance = q.popleft()
                q_sz-=1

                if node not in self.graph:
                    continue
            
                for each_neighbour in self.graph[node]:
                    curr_node, node_distance = each_neighbour[0], each_neighbour[1]

                    # We only traverse those nodes where we think the distance is minium or better than current
                    # This makes sure we don't traverse towards a back edge
                    # Cause a back edge will have distance more when we count for a backward so we won't push it in queue.
                    # Also we don't take those paths where distance is more than its already computed.

                    if self.dist[curr_node] > distance + node_distance:
                        self.dist[curr_node] = distance + node_distance
                        q.append((curr_node, self.dist[curr_node]))
                
            curr_stop += 1
            
        return self.dist[dest]
