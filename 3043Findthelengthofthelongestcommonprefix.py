class trie:
    def __init__(self):
        self.children = [None] * 10
    

    def get_idx(self, s):
        return ord(s) - ord('0')


    def insert(self, s):
        root = self

        for each_s in s:
            idx = self.get_idx(each_s)

            if not root.children[idx]:
                root.children[idx] = trie()
            
            root = root.children[idx]
        
        root.end_of_string = True
    

    def prefix_search(self, s):
        ln = 0
        root = self

        for each_s in s:
            idx = self.get_idx(each_s)
            if not root.children[idx]:
                return ln
                
            ln+=1
            root = root.children[idx]
        
        return ln


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        max_ln = 0
        arr2 = sorted(arr2, reverse=True)

        """
            The trick to solve this question is through a trie.
            We make a trie for arr1. So m if length of arr with max d as the digit.
            We have m*d computation.
            Now for arr2 we do a prefix search so we do n*d where n is length of the arr2.
            So O(m*d + n*d) is the time complexity.
            Space complexity is O(m*d)
        """

        tr = trie()

        for each_nm in arr1:
            tr.insert(str(each_nm))

        for each_nm in arr2:
            ln = len(arr2)
            
            if max_ln > ln:
                break

            max_ln = max(max_ln, tr.prefix_search(str(each_nm)))
        
        return max_ln
