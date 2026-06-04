class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        self.intervals = intervals
        left_idx = self.upper_boundl(newInterval[0])
        right_idx = self.upper_boundr(newInterval[1])

        left_new = newInterval[0]
        right_new = newInterval[1]

        if left_idx == right_idx:
            return intervals
        
        new_lst = []
        
        if left_idx < 0 and right_idx >= len(self.intervals):
            return [newInterval]

        elif left_idx < 0:
            left_final = left_new

            if right_new >= intervals[right_idx][0]:
                new_lst.append([left_final, intervals[right_idx][1]])
                for j in range(right_idx + 1, len(intervals)):
                    new_lst.append(intervals[j])
            else:
                new_lst.append([left_final, right_new])
                for j in range(right_idx, len(intervals)):
                    new_lst.append(intervals[j])
            
            return new_lst
        
        elif right_idx >= len(self.intervals):

            right_final = right_new

            for j in range(left_idx):
                new_lst.append(intervals[j])

            if left_new <= intervals[left_idx][1]:
                new_lst.append([intervals[left_idx][0], right_final])
            else:
                new_lst.append(intervals[left_idx])
                new_lst.append([left_new, right_final])
            
            return new_lst

        for i in range(left_idx):
            new_lst.append(intervals[i])

        final_lft = intervals[left_idx][0]
        final_rgt = intervals[right_idx][1]

        # First lets check the left index if its within the bounds
        if left_new <= intervals[left_idx][1]:
            final_lft = intervals[left_idx][0]

            # If we can fit the new interval in the extreme right interval
            if right_new >= intervals[right_idx][0]:
                final_rgt = intervals[right_idx][1]
                new_lst.append([final_lft, final_rgt])
            else:
                new_lst.append([final_lft, right_new])
                new_lst.append(intervals[right_idx])
        else:
            new_lst.append(intervals[left_idx])

            # The left interval is not in range so we need to put the left as a new element
            # Now lets check if the right is in range
            if right_new >= intervals[right_idx][0]:
                new_lst.append([left_new, intervals[right_idx][1]])
            else:
                # If it is less than the interval then this is a new element and we need to insert right also
                new_lst.append([left_new, right_new])
                new_lst.append(intervals[right_idx])

        for j in range(right_idx + 1, len(intervals)):
            new_lst.append(intervals[j])
        
        return new_lst


    def upper_boundl(self, val):
        l = 0
        r = len(self.intervals) - 1
        md = 0

        while r - l >= 0:
            md = (l + r) // 2
            if self.intervals[md][0] == val:
                return md
            elif self.intervals[md][0] < val:
                l = md + 1
            else:
                r = md - 1
            
        return r
    

    def upper_boundr(self, val):
        l = 0
        r = len(self.intervals) - 1
        md = 0

        while r - l >= 0:
            md = (l + r) // 2
            if self.intervals[md][1] == val:
                return md
            elif self.intervals[md][1] < val:
                l = md + 1
            else:
                r = md - 1
            
        return l
