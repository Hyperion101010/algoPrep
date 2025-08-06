class Solution:
    def numDecodings(self, s: str) -> int:
        # Building a lookup table for DP
        self.lkup = [ -1 for i in range(len(s)+1)]
        self.ln = len(s)
        self.s = s
        ans = self.vst(0)
        return ans
    
    def vst(self, idx):
        """
            The way this recursion is working is,
            it only considers a solution as valid if
            1. The end index call of the function is valid,
            then in this case we return 1 (valid decode)
            2. The index call if it exceeds the index of string then also,
            count as 1 since it might be case of the call of considering two digits at once.
            
            Eg.
            Let's consider 226

            Decoding -
            22 ------> 6 --------> return 1 (seq is 22 | 6)
            2 --------> 26 -------> return 1 (seq is 2 | 26)
            2 ------> 2 -------> 6 return 1 (seq is 2 | 2 | 6)

            Thus, we never count while branching out our decoding.
            We only count at the end when we hit the decoding limit.
            For scenarios that are invalid like the once containing 0 we just return 0.
        """

        # End of count return 1 since it must be valid to reach end of string.
        if idx >= self.ln:
            return 1
        
        # End of count return 1 since it must be valid to reach end of string.
        if idx == self.ln - 1:
            # End of count return 0 since this case is invalid.
            if int(self.s[idx]) != 0:
                return 1
            else:
                return 0
        
        # Case of index being 0 and digit starts with 0 which is invalid.
        if idx == 0 and int(self.s[idx]) == 0:
            return 0
            
        # Case of lookup already present then return the result.
        if self.lkup[idx] > -1:
            return self.lkup[idx]
        
        # Case of possibility to check 2 digits at once. Now we can branch out.
        if self.ln - idx > 1:
            # Return invalid case as 0.
            if int(self.s[idx]) == 0:
                self.lkup[idx] = 0
                return self.lkup[idx]
            else:
                # Case that its valid now count 2 branches.
                # One branch considering one index at once.
                # Other branch considering two index at once.
                nm = int(self.s[idx:idx+2])
                nm1 = 0
                if nm <= 26 and nm > 9:
                    nm1 = self.vst(idx + 2)
                nm2 = self.vst(idx + 1)

                # Add both branch counts
                self.lkup[idx] = nm1 + nm2
        
        # Return lookedup result using DP.
        return self.lkup[idx]
