class Solution:
    def traverse(self, start_idx):
        if start_idx < 0:
            return True
        
        if self.dp[start_idx] is not None:
            return self.dp[start_idx]
        
        match = False

        for each_word in self.word_dict:
            # We first check if the current word is matched.
            if each_word == self.s[start_idx - len(each_word) + 1: start_idx + 1]:
                # If the word is matched then we check for the sub word to match.
                if self.traverse(start_idx - len(each_word)):
                    # If both word matches then we return True.
                    self.dp[start_idx] = True
                    return True

        self.dp[start_idx] = match

        return self.dp[start_idx]


    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.s_ln = len(s)
        self.word_dict = wordDict
        self.s = s
        self.dp = [None for i in range(len(s))]

        return self.traverse(len(s) - 1)

"""
class Solution:
    def is_possible(self, a):
        for each_word in self.word_dict:
            if a == each_word:
                return True
        
        return False
    

    def traverse(self, start_idx, end_idx):
        if end_idx == self.s_ln - 1:
            if self.is_possible(self.s[start_idx: end_idx + 1]):
                return True

            return False
        
        if self.dp[end_idx] is not None:
            return self.dp[end_idx]

        next_answers = False
        if self.is_possible(self.s[start_idx: end_idx + 1]):
            next_answers = self.traverse(end_idx + 1, end_idx + 1)
        else:
            next_answers = self.traverse(start_idx, end_idx + 1)

        self.dp[end_idx] = next_answers
        return self.dp[end_idx]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.s_ln = len(s)
        self.word_dict = wordDict
        self.s = s
        self.dp = [None for i in range(len(s))]
        return self.traverse(0, 0)
"""

"""
class Solution:
    class Trie:
        def __init__(self):
            self.children = [None] * 26
            self.end_of_string = False
        
        def get_idx(self, char):
            return ord(char) - ord('a')

        def insert(self, value):
            root = self

            for i in value:
                idx = root.get_idx(i)
                if root.children[idx] is None:
                    root.children[idx] = Solution.Trie()
                
                root = root.children[idx]
            
            root.end_of_string = True
        

        def search(self, value):
            root = self

            for i in value:
                idx = root.get_idx(i)
                if root.children[idx] is None:
                    return False
            
                root = root.children[idx]
            
            return True


    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = self.Trie()

        for each_word in wordDict:
            root.insert(each_word)

        total_length = 0

        start_idx = 0
        end_idx = 0

        while end_idx < len(s):
            if root.search(s[start_idx:end_idx+1]):
                total_length += end_idx - start_idx + 1
                start_idx = end_idx + 1
            
            end_idx += 1
        
        if total_length == len(s):
            return True
        
        return False
"""
