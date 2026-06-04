import heapq

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        self.heap = intervals

        heapify(self.heap)

        self.temp_lst = []

        """
            In this problem we will simulate the process of merging two intervals.
            So to simulate the process we use min heap and we first take out the first two elements.
            Then we see if they can be merged, if they can then we put it in the heap again as it will be reused as first elements for the next iteration from the heap.
            If they cannot be merged then we put them in another list.
            Since they are sorted this list will always be sorted.
            Finally we push everything from the leftover heap into this temp list and return it.
        """

        while len(self.heap) >= 2:
            first_pair = heappop(self.heap)
            second_pair = heappop(self.heap)

            if second_pair[0] <= first_pair[1]:
                edge = max(first_pair[1], second_pair[1])
                heappush(self.heap, [first_pair[0], edge])
            else:
                self.temp_lst.append(first_pair)
                heappush(self.heap, second_pair)

        if len(self.heap) == 0:
            return self.temp_lst

        self.temp_lst.append(self.heap[0])

        return self.temp_lst

