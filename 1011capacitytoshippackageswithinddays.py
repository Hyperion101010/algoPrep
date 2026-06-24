class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        sm = 0
        lft = -1

        self.days = days
        self.weights = weights

        """
            The crux of the problem is finding a number that does the best job of getting all days used.
            We can apply a binary search for the range max(weight) to sum of weight.
            This is cause we will find a valid solution between these numbers as max should acomodate for all containers on ship.
            And sum of weights will accomodate for all containers with just 1 day itself.
            We run a binary search between these ranges and for that we check if each weight can satisfy us with if any days remaining.
            Then we keep running this search until we finish our search.
            We return the index greater than or equal to the target so that the solution is always possible.
        """
        for each_nm in weights:
            if each_nm > lft:
                lft = each_nm
            
            sm += each_nm
        
        lft = lft
        rgt = sm
        md = 0

        while rgt - lft >= 0:
            md = (lft + rgt) // 2

            total_days_needed = self.check_for_val(md)

            # If we can fulfill in the md weight then we found the exact answer.
            #if total_days_needed == 0:
            #    return md
            # Don't early return cause there can be better solutions possible.
            # If we can fulfill in less days than the weight then we can surely decrease the weight.
            if total_days_needed >= 0:
                rgt = md - 1
            # If it needs more days than actual then we should increase the weight.
            else:
                lft = md + 1
        
        return lft


    def check_for_val(self, wgt):

        start_idx = 0
        end_idx = 0
        d = self.days

        sm = 0

        while end_idx < len(self.weights):

            # If weight greater than the needed, then we don't consider the current ship.
            if sm + self.weights[end_idx] > wgt:
                start_idx = end_idx
                sm = 0
                d -= 1
            # If weight equals the new addition then we start from next idx.
            elif sm + self.weights[end_idx] == wgt:
                start_idx = end_idx + 1
                end_idx += 1
                sm = 0
                d -= 1
            else:
                sm += self.weights[end_idx]
                end_idx += 1
        
        if sm <= wgt and sm > 0:
            d -= 1

        return d
