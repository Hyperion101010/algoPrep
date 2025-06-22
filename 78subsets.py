class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        lst = []
        lst.append([])
        for i in nums:
            tmp_lst = lst[:]
            for j in lst:
                ll = j[:]
                ll.append(i)
                tmp_lst.append(ll)
            lst = tmp_lst[:]
        return lst
