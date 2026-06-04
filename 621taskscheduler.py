import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        lkup = {}
        self.rem_proc_list = []

        # First counting the tasks per label
        for each_label in tasks:
            if each_label not in lkup:
                lkup[each_label] = 1
            else:
                lkup[each_label] +=1
        
        # Keeping the track of elements per count
        self.heap = []
        for k, v in lkup.items():
            self.heap.append((-v, k))

        heapify(self.heap)

        cnt = 0
        past_label = -1
        while len(self.heap) > 0:

            self.new_heap = []

            heap_len = len(self.heap)

            itr = 0
            """
                The idea is we consider the CPU allocation as a task of assigning more frequency tasks first.
                We will consider one successful allocation as n + 1 cause that's what we can do maximum work including cooldown.
                Then we run a loop till either of them finishes and then we calculate the timings.
            """
            while itr < n + 1 and len(self.heap) > 0:
                freq, temp_label = heappop(self.heap)
                
                lkup[temp_label] -= 1
                if lkup[temp_label] > 0:
                    self.new_heap.append((-lkup[temp_label], temp_label))
                itr+=1
            
            for i in self.heap:
                self.new_heap.append(i)

            #  If we exited due to covering all labels then
            if len(self.heap) == 0:
                # If this is our last iteration then we only need to add how much we processed
                if len(self.new_heap) == 0:
                    cnt += heap_len
                else:
                    # If some task is left then this is definitely < delay so total time required is n+1 atleast.
                    cnt += n+1
            else:
                cnt += n+1

            self.heap = self.new_heap
            heapify(self.heap)

        return cnt
