class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt = 0
        prd = 1
        for i in nums:
            if i == 0:
                zero_cnt +=1
            else:
                prd *= i
        
        lst = []
        for i in range(len(nums)):
            if zero_cnt >= 2:
                lst.append(0)
            elif zero_cnt == 1:
                if nums[i] == 0:
                    lst.append(prd)
                else:
                    lst.append(0)
            else:
                lst.append(int(prd/nums[i]))
        return lst
