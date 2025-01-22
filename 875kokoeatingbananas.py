import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lst = sorted(piles)

        # Our max element which is our upper bound of search
        mx = lst[len(piles)-1]

        # We are starting with k = 1 and then proceed towards k = max(pile)
        lft = 1
        rgt = mx

        idx = -1

        print(lft, rgt)

        # Now consider that at each step we run over the entire piles array and calculate the h that we will require
        while rgt >= lft:
            md = floor(lft + (rgt - lft)/2)

            tt = 0

            # ceil of each pile by k gives us the total amount of hours required.
            for each_pile in piles:
                tt += math.ceil(each_pile/md)
            
            # We are searching for a lower bound
            # So we always store the values where we get it lesser than or equal to h

            print(md, tt, h)

            # In this case we are choosing first a value of k and storing it.
            # Now then when done I move my rgt again to a lower bound.
            # Then I check if it again satisfies the condition and thus I'll again update it.
            # Thus finally I'll have choosen the minimal amount of idx 'k' value.
            if tt <= h:
                idx = md
                rgt = md - 1
            else:
                lft = md + 1
        return idx
