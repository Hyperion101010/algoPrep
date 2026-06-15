class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        lkup = [-1 for i in range(26)]

        """
            We are going to follow a two pointer approach for this problem.
            First we start with storing the last index the character is found.

            Now we start a two pointer with start_index and end_index.
            We move end_index pointer one by one, while keeping a max var to store the last index we need to cut this parition.
            Now when we cut the paritition we push it in list and keep going.
        """

        for i in range(len(s)):
            char = s[i]
            idx = ord(char) - ord('a')
            lkup[idx] = max(lkup[idx], i)
        
        start_idx = 0
        end_idx = 0
        mx = -1

        lst = []

        while end_idx < len(s):
            last_known_idx = ord(s[end_idx]) - ord('a')
            
            if mx == -1:
                mx = lkup[last_known_idx]

            if lkup[last_known_idx] > mx:
                mx = lkup[last_known_idx]

            if end_idx == mx:
                lst.append(end_idx - start_idx + 1)
                end_idx += 1
                start_idx = end_idx
                mx = -1
                continue
            
            end_idx += 1
        
        return lst
