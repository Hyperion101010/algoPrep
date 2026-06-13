class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        lkup = {}

        """
            The crux of the problem is can we make a simulation which performs the grouping on the go.
            So we first maintain a set of elements.
            We also maintain a count of each number.
            We finally put everything in a min heap.
            Now we check if len of array is divisible by the group size, if not then we return False.
            If divisible, then remove one from the array and keep going till the count.
            If everything fine then again put the remaining in the heap.
            Again continue.
        """

        elements = set()

        for i in hand:
            if i in lkup:
                lkup[i] +=1
            else:
                lkup[i] = 1
        
            elements.add(i)
        
        if len(hand) % groupSize != 0:
            return False
        
        self.pq = list(elements)
        heapify(self.pq)

        while len(self.pq) > 0:

            total_cnt = groupSize
            past_nm = -1

            temp_lst = []

            while total_cnt > 0:

                if len(self.pq) == 0:
                    return False

                next_ele = heappop(self.pq)
                if past_nm != -1 and next_ele != past_nm + 1:
                    return False
                
                past_nm = next_ele
                lkup[next_ele] -=1

                if lkup[next_ele] > 0:
                    temp_lst.append(next_ele)

                total_cnt -=1
            
            for i in temp_lst:
                heappush(self.pq, i)
            
        return True
