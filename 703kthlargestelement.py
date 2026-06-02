import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums

        # If length of array greater than k        
        heapq.heapify(self.heap)
        self.k = k

    def add(self, val: int) -> int:
        if len(self.heap) == 0:
            heappush(self.heap, val)
            return self.heap[0]

        if len(self.heap) < self.k:
            heappush(self.heap, val)
            return self.heap[0]
        
        # Maintaining an array of only k elements with 0 as the kth largest element
        while len(self.heap) > self.k:
            heappop(self.heap)
        
        if val >= self.heap[0]:
            heappush(self.heap, val)
            heappop(self.heap)
        
        return self.heap[0]

    """
    def __init__(self, k: int, nums: List[int]):
        self.heap = sorted(nums)
        self.k = k
        idx = len(nums) - 1
        while idx > 0 and idx > len(nums) - k:
            idx-=1
        
        if idx < 0:
            idx = 0
        self.k_idx = idx


    def floor_search(self, val):
        lf = 0
        rgt = len(self.heap) - 1
        md = 0

        while rgt - lf >= 0:
            md = (lf + rgt) // 2
            if val == self.heap[md]:
                return md
            elif val > self.heap[md]:
                lf = md + 1
            else:
                rgt = md - 1
        
        # lf is always the upper bound, when we need to find an index for val >= val in array
        # Find either the same value index or next index.
        # Messed up the solution due to incorrect upper bound on binary search
        return lf


    def add(self, val: int) -> int:
        # Get me index of one plus than the element index. 
        idx = self.floor_search(val)

        if len(self.heap) == 0:
            self.heap.insert(0, val)
            return self.heap[self.k_idx]
        
        if len(self.heap) < self.k:
            self.heap.insert(idx, val)
            return self.heap[self.k_idx]

        if val >= self.heap[self.k_idx]:
            self.heap.insert(idx, val)
            if self.k_idx < len(self.heap) - 1:
                self.k_idx+=1
        else:
            self.heap.insert(self.k_idx, val)
            self.k_idx+=1
        return self.heap[self.k_idx]
    """
