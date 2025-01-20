class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lkup_s1 = dict()

        # First count all the elements in s1 that we have to track
        for s in range(len(s1)):
            if s1[s] in lkup_s1.keys():
                lkup_s1[s1[s]] +=1
            else:
                lkup_s1[s1[s]] =1

        fst = 0
        lst = len(s1) - 1

        # Case when the first s1 is greater than s2, this case we can't really have s1 as substring of s2 so its invalid
        if len(s1) > len(s2):
            return False
        
        tmp_lst = 0

        lkup = dict()

        # Then track elements only within the window that we are tracking, keep the right most lst pointer for later usage
        while tmp_lst < len(s1) - 1:
            if s2[tmp_lst] in lkup.keys():
                lkup[s2[tmp_lst]] +=1
            else:
                lkup[s2[tmp_lst]] =1
            tmp_lst +=1

        
        while lst < len(s2):

            # Take our lst pointer, here we are adding the keys pointed by our current lst pointer.
            if s2[lst] in lkup.keys():
                lkup[s2[lst]] +=1
            else:
                lkup[s2[lst]] =1
            
            found = True

            # Here we are checking for all elements present in our windo
            # We skip checks when the value v is equal to 0.
            # In other cases we check if key is present in both of the maps and the frequency is same.
            for k, v in lkup.items():
                # Don't check condition for when we don't really have the frequency
                if v == 0:
                    continue

                if k in lkup_s1.keys() and (lkup[k] == lkup_s1[k]):
                    pass
                else:
                    # Now we do have an element but we don't have correct freq, so this is incorrect.
                    found = False
            
            if found:
                return True

            # Only fst pointer freq needs to be deleted because this is now not in our window.
            # The lst pointer freq is still in our window so we increment it and add the new position pointed by it
            # At the start of the while loop as mentioned earlier,
            lkup[s2[fst]]-=1
            
            fst +=1
            lst +=1
            
        return False
