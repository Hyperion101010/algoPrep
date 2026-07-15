class Solution:
    def populate_sequences(self, s):
        lst = [s[i] for i in range(len(s))]

        for each_idx in range(len(s)):
            past_chr = lst[each_idx]
            lst[each_idx] = '*'

            new_str = ''.join(lst)

            if new_str in self.table:
                self.table[new_str].append(s)
            else:
                self.table[new_str] = [s]

            lst[each_idx] = past_chr

    
    def traverse(self, beginWord: str, endWord: str):        
        mn = 1e9
        visited = {}
        visited[beginWord] = True

        q = deque([])
        q.append((beginWord, 1))

        while len(q) > 0:
            curr_word, depth = q.popleft()

            if curr_word == endWord:
                mn = min(mn, depth)

            # Explore all its possible sub-sequences.
            lst = [curr_word[i] for i in range(len(curr_word))]

            for each_idx in range(len(curr_word)):
                prev_s = curr_word[each_idx]
                lst[each_idx] = '*'

                new_str = ''.join(lst)

                if new_str in self.table:
                    # For each sequence having matching strings we put it in the queue.
                    for each_ngb in self.table[new_str]:
                        if each_ngb not in visited:
                            q.append((each_ngb, depth + 1))
                            visited[each_ngb] = True
                    
                    #self.table[new_str] = []

                lst[each_idx] = prev_s

        return mn


    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        self.table = {}

        """
            The crux of the problem is we start with a beginWord.
            From the beingWord we generate all possible sequence with one change as:
            For eg: hot we generate *ot, h*t, ho*
            Now for each sequence we keep a table in place to store them.
            So *ot = [hot]. 
            This is how we will map the sequence to the input as well as all other words that match to this sequence.
            So now, first we need to create a table of all of these elements.
            This table we will use during our BFS.

            Now for our BFS, we start with our beginWord and also maintain a visited dict to mark the visited nodes.
            So first we put the beginWord and depth as 1 with it.

            Then we generate all its sequences and put all the words for this sequence into the queue.
            We also add depth + 1 before putting them so that we know at which depth this occurs.

            Now after doing all the changes, our algorithm would work in a logic:
            1. First generate all sequence and find all words possible to be nearest to this word.
            2. Put all found words in queue and then explore all subsequences for this queue.
            3. In this fashion when we get the endWord keep collecting the minimum depth.
            Then return the final answer.

            The time complexity is:
            For word: N, we need L times to generate sequence and list join costs L.
            So N * L * L = N * L^2 is the time complexity.
            So, the time complexity is O(NL^2)

            We keep a map of L sequence with N words.
            Queue is N so the space complexity is O(NL)
        """
        for each_word in wordList:
            if each_word == beginWord:
                continue
            else:
                self.populate_sequences(each_word)
        
        begin_word_lst = [beginWord[i] for i in range(len(beginWord))]

        dist = self.traverse(beginWord, endWord)

        if dist >= 1e9:
            return 0
        
        return dist

"""
class Solution:
    def is_valid(self, s1, s2):
        cnt = 0

        for each_idx in range(len(s1)):
            if s1[each_idx] != s2[each_idx]:
                cnt +=1
        
        if cnt > 1:
            return False
        
        return True

    
    def traverse(self, begin: str, endword: str):
        self.dist = {}
        
        for each_item in self.graph.keys():
            self.dist[each_item] = 1e9

        self.dist[begin] = 1

        self.q = deque([])
        self.q.append(begin)

        while len(self.q) > 0:
            ele = self.q.popleft()

            if ele in self.graph:
                for each_word in self.graph[ele]:
                    if self.dist[ele] + 1 < self.dist[each_word]:
                        self.dist[each_word] = self.dist[ele] + 1
                        self.q.append(each_word)
        
        return self.dist[endword]


    def add_edge(self, a, b):
        if a not in self.graph:
            self.graph[a] = [b]
        else:
            self.graph[a].append(b)


    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        self.graph = {}

        total_words = len(wordList)

        for each_word in wordList:
            for each_other_word in wordList:
                if each_word != each_other_word and self.is_valid(each_word, each_other_word):
                    self.add_edge(each_word, each_other_word)
                    self.add_edge(each_other_word, each_word)
        
        if beginWord not in self.graph:
            for eachWord in wordList:
                if self.is_valid(beginWord, eachWord):
                    self.add_edge(beginWord, eachWord)
                    self.add_edge(eachWord, beginWord)

        if beginWord not in self.graph:
            return 0
        if endWord not in self.graph:
            return 0

        dist = self.traverse(beginWord, endWord)

        if dist >= 1e9:
            return 0
        
        return dist
"""
