class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.parent = [i for i in range(2000)]

        lkup = {}
        lst = []

        for each_edge in edges:
            a = each_edge[0]
            b = each_edge[1]

            # Why can't we use self.parent instead of self.find for this case?
            # So the reason to use self.find rather than self.parent is
            # In union operation we connect the super parents of the both sets and not the direct parents.
            # So checking the parents before and after operation will need to stale parents and thus incorrect result.
            # Thus use find which always leads to the same root parent always.
            # Now the lookup for a and b helps cause a loop will only happen if we are already adding the edges on
            # which an operation has already happened.
            before_start_a = self.find(a)
            before_start_b = self.find(b)
            self.union(a, b)
            after_a = self.find(a)
            after_b = self.find(b)
            if a in lkup and b in lkup and (before_start_a == after_a and before_start_b == after_b):
                lst.append(each_edge)
            
            lkup[a] = 1
            lkup[b] = 1

        if len(lst) >= 1:
            return lst[-1]
        
        return lst

    def union(self, a, b):
        set_a = self.find(a)
        set_b = self.find(b)

        if set_a != set_b:
            self.parent[set_b] = set_a
    
    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        
        return self.parent[a]

    """
        self.graph = {}

        for each_edge in edges:
            a = each_edge[0]
            b = each_edge[1]
            self.add_edge(a,b)
            self.add_edge(b,a)

        return self.dfs(edges[0][0])

    def add_edge(self, a, b):
        if a not in self.graph:
            self.graph[a] = [b]
        else:
            self.graph[a].append(b)


    def dfs(self, a):
        queue = []
        parent = {}
        lkup = {}

        queue.append(a)
        parent[a] = -1

        lst = []

        while len(queue) > 0:
            start_node = queue.pop()
            lkup[start_node] = 1

            # Visiting its neighbours
            for i in self.graph[start_node]:
                # Check if this neighbour is backward connection
                if i == parent[start_node]:
                    continue

                # If this parent is set that means this node was already visited.
                # This could only mean a cycle.
                if i in parent:
                    lst.append([start_node, i])
                else:
                    queue.append(i)
                    parent[i] = start_node

        if len(lst) > 1:
            return lst[-1]
        
        return lst
    """
