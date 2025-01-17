class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        fst = 0
        mx = 0
        lst = fst

        # Lookup table that is actually a window that mentions the count of chars
        lkup = dict()
        while lst < len(s):

            # Check if we have the key already in the table (entry already present but can be 0 as well)
            if s[lst] in lkup.keys():
                # If lkup is > 0 that means its already present in the lkup
                # so its a repeated character, now we calculate the substring length
                # In out case its lst - fst not lst - fst since we believe that lst will be different than fst 
                if lkup[s[lst]] > 0:
                    ln = lst - fst
                    mx = max(mx, ln)
                    lkup[s[fst]] -= 1
                    fst+=1
                    continue
                # This means it is not present in our window and has not yet been repeated, so just add the occurence
                else:
                    lkup[s[lst]] += 1
            # Create key entry in the table.
            else:
                lkup[s[lst]] = 1
            lst+=1
        
        # Case when we have bbbbb or just same char repeating
        if mx == 0 and fst == 0:
            mx = max(mx, len(s))
        # Case when the string itself is empty
        if lst == 0:
            mx = 0
        # Case of aab, now in this case the updated length will never be update into the max var.
        # So in this case we check if its really bigger than mx and we update it.
        # So for aab its like mx = 1 earlier and lst = 2+1 (at end) fst = 1, so lst - fst = 2
        if (lst - fst) > mx:
            mx = ( lst - fst )
        return mx
