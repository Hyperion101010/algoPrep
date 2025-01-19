class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        fst = 0
        lst = 0
        lkup = dict()
        mx_freq = 0
        ln = 0
        mx = 0

        # The solution to this problems is
        # Have a first pointer that points to the start of window
        # Have a last pointer that points to the last position in the window
        # When there is a condition that our number of changes 'k' are exhausted then we store it as max(ln-1, mx) (exhausted at 'i+1' th)
        # Then after all of this is done, we check if mx is 0 that means it was never updated
        # At last we also check for a case when the last substring is like ABAA and k=0, then we will never have condition max(ln-1, mx) so we update it to the substring length (lst - fst)
        while lst < len(s):
            ln +=1
            if s[lst] in lkup.keys():
                # First add freq in our lkup
                lkup[s[lst]] += 1
            else:
                lkup[s[lst]] = 1
            
            if mx_freq < lkup[s[lst]]:
                mx_freq = lkup[s[lst]]

            #print(mx_freq, ln, k, fst, lst, lkup)
            
            if ln - mx_freq > k:

                # Minus one cause in our scenario its a case when the current index is outside of the window
                mx = max(mx, ln-1)

                # Decrement the count for our window first pointer
                lkup[s[fst]]-=1

                # Update the max freq counter based on our conditions
                mx2 = 0
                for _, v in lkup.items():
                    mx2 = max(mx2, v)
                mx_freq = mx2

                ln-=1
                fst+=1

            lst+=1
        
        # Case when we have a repeating sequence like bbbb, in this case we end up never updating the mx variable
        if mx == 0:
            mx = (lst - fst)

        # Case ABAA
        # In this case when we are calculating the case to exit checking and update variable then we have to check for this case at the end. That is AA case.
        if ln - mx_freq >=k:
            mx = max(mx, ln)
        return mx
