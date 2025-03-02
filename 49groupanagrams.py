class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        """
        The key is we start the problem by sorting each element on the basis of its entries.
        We store every sorted elements sorted character by character inside a list.
        We then run a loop over the elements where we put the each occurence of original string inside a map.
        This map has key as one of the sorted element and then its value as the original string.
        Then finally we iterate over the map and just return the answer.
        """
        sort_lst = []
        for i in strs:
            tmp = []
            for j in i:
                tmp.append(j)
            
            # We create a list of sorted chars, word by word.
            sort_lst.append(sorted(tmp))
        
        # The map to save our counts.
        ans = dict()
        for i in range(len(sort_lst)):
            tmp = ""

            # First check if the list we create is possible in the map.
            for each_char in sort_lst[i]:
                tmp = tmp + each_char

            # Insert the original string in map if the key is possible.
            if tmp in ans.keys():
                ans[tmp].append(strs[i])
            else:
                ans[tmp] = [strs[i]]
        
        # Populate the answer in a list and return.
        res = []
        for k, v in ans.items():
            res.append(v)
        return res
