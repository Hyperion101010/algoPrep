class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        self.lfinish_time = []
        self.bfinish_time = []

        """
            The crux of the problem is we first sort of the land and rides by the earliest time.
            Then we check for land if selecting the first and then water among all rides is a valid option.
            Then we check for water first and then see if selecting land after it is a valid option.
            Thus we return the minimum of the both options.
        """

        for each_idx in range(len(landStartTime)):
            self.lfinish_time.append([landStartTime[each_idx] + landDuration[each_idx], each_idx])
        
        for each_idx in range(len(waterStartTime)):
            self.bfinish_time.append([waterStartTime[each_idx] + waterDuration[each_idx], each_idx])

        self.lfinish_time = sorted(self.lfinish_time)
        self.bfinish_time = sorted(self.bfinish_time)

        option1 = self.lfinish_time[0][0]
        option2 = self.bfinish_time[0][0]

        # First lets find the index with the time in water
        option1_idx = self.binary_search(waterStartTime, option1)

        # Traverse through each water slide to find which boat leads to the least time.
        temp_option = 1e9
        for each_idx in range(len(waterStartTime)):
            if waterStartTime[each_idx] < option1:
                temp_option = min(temp_option, waterDuration[each_idx])
            else:
                temp_option = min(temp_option, (waterStartTime[each_idx] - option1) + waterDuration[each_idx])
        
        option1 += temp_option

        temp_option = 1e9

        option2_idx = self.binary_search(landStartTime, option2)

        for each_idx in range(len(landStartTime)):
            if landStartTime[each_idx] < option2:
                temp_option = min(temp_option, landDuration[each_idx])
            else:
                temp_option = min(temp_option, (landStartTime[each_idx] - option2) + landDuration[each_idx])

        option2 += temp_option

        return min(option1, option2)
    
    

    # Need to search for the closest element to this time in the respective array.
    def binary_search(self, arr, val):
        lft = 0
        rgt = len(arr) - 1
        md = 0

        while rgt - lft >= 0:
            md = (lft + rgt) // 2

            if arr[md] == val:
                return md
            elif val > arr[md]:
                lft = md + 1
            else:
                rgt = md - 1

        if lft >= len(arr):
            return len(arr) - 1

        return lft
            
