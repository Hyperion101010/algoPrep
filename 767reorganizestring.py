import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:

        """
            The whole point of this question is we select the characters based on the count.
            We put everything in the heap.
            We get things out of the heap and then always select the most element and not in the s at the end.
            If we are able to put them and continue then we keep doing it.
            If the heap is exhausted then we just can't do anything.
        """
        
        self.pq = []

        lkup = {}

        for i in s:
            if i in lkup:
                lkup[i] += 1
            else:
                lkup[i] = 1
        
        for k, v in lkup.items():
            self.pq.append((-v, k))
        
        heapq.heapify(self.pq)

        s = ""

        while len(self.pq) > 0:

            if len(s) > 0:
                end_char = s[-1]

                first_cnt, first_char = heappop(self.pq)

                if end_char == first_char:
                    if len(self.pq) == 0:
                        return ""
                    else:
                        second_cnt, second_char = heappop(self.pq)

                        heappush(self.pq, (first_cnt, first_char))

                        second_cnt = -second_cnt
                        second_cnt -= 1

                        s += second_char

                        if second_cnt > 0:
                            heappush(self.pq, (-second_cnt, second_char))

                else:
                    first_cnt = -first_cnt
                    first_cnt -= 1
                    
                    s += first_char

                    if first_cnt > 0:
                        heappush(self.pq, (-first_cnt, first_char))

            else:
                cnt, char = heappop(self.pq)

                cnt = -cnt
                cnt -=1
                s += char

                if cnt > 0:
                    heappush(self.pq, (-cnt, char))
            
        return s
