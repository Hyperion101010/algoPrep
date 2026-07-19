class Solution:
    def add_edge(self, a, b):
        if a in self.graph:
            if b not in self.graph[a]:
                self.graph[a].append(b)
        else:
            self.graph[a] = [b]


    def build_graph(self, past_str, curr_str) -> None:
        ln = min(len(past_str), len(curr_str))

        idx = 0

        while idx < ln:
            if past_str[idx] == curr_str[idx]:
                pass
            else:
                self.add_edge(past_str[idx], curr_str[idx])
                break
            idx += 1
        
        if idx == ln and len(past_str) > len(curr_str):
            self.invalid = True


    def toposort(self):

        self.q = deque([])

        for k, v in self.indegree.items():
            if self.indegree[k] == 0:
                self.q.append(k)
        
        while len(self.q) > 0:
            curr_ele = self.q.popleft()
            self.ans.append(curr_ele)
            self.cnt +=1

            if curr_ele in self.graph:
                for each_ngb in self.graph[curr_ele]:
                    self.indegree[each_ngb] -= 1

                    if self.indegree[each_ngb] == 0:
                        self.q.append(each_ngb)
        
        return



    def alienOrder(self, words: List[str]) -> str:
        self.graph = {}
        self.invalid = False

        for each_idx in range(1, len(words)):
            self.build_graph(words[each_idx - 1], words[each_idx])

        """
            The crux of the problem is to first create a graph.
            So we take two consecutive strings, then for those strings we check if both are prefix.
            If both are prefix then we take those string which are not matching and we append in the graph.

            In this fashion we will end up with a graph where each string is in some sorted order.
            Now only those chars are needed since, other chars we can assume they have indegree as 0 itself.

            Now while prefix and building the graph we will end up with some cases "abc", "ab" now this is invalid so we mark it.

            This manner we do a graph construction.

            Now we run a topological sort.

            Now if our topological sort is not able to visit all edges then it means there is a loop.
            So, this is an invalid case as well.

            Finally, we return the answer.
        """
        
        lkup = set()
        self.ans = []

        for each_word in words:
            for each_s in each_word:                
                lkup.add(each_s)
        
        self.indegree = {}

        for each_s in lkup:
            self.indegree[each_s] = 0

        for each_letter, each_lst in self.graph.items():
            for each_ngb in each_lst:
                self.indegree[each_ngb] += 1
        
        self.cnt = 0

        self.toposort()

        if self.invalid:
            return ""

        if self.cnt != len(lkup):
            return ""

        return "".join(self.ans)
