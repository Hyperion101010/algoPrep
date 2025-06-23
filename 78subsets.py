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


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.op = []
        self.backtrack(0, [], nums)
        return self.op

    def backtrack(self, idx, curr, nums):
        self.op.append(curr[:])
        for i in range(idx, len(nums)):
            """
            The way this works is first we call with 
            backtrack(0, [], [1,2,3])

            this goes in for loop
            backtrack(1, [1], [1,2,3])
            curr = [1]

            curr = [1, 2] idx = 2 means element is 3

            again backtrack, curr = [1,2,3] idx = 3 end here

            pop [1]

            add [2]

            curr = [2]

            curr = [2, 3] add in op

            pop [2]

            add [3]

            curr =[3] add in op

            thus finally we add all elements in the list

            0 [[]] [] 0


            1 [[], [1]] [1] 1


            2 [[], [1], [1, 2]] [1, 2] 2


            1 [[], [1], [1, 2], [1, 2, 3]] [1] 2


            0 [[], [1], [1, 2], [1, 2, 3], [1, 3]] [] 1


            2 [[], [1], [1, 2], [1, 2, 3], [1, 3], [2]] [2] 2


            0 [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3]] [] 2
            """

            curr.append(nums[i])
            self.backtrack(i + 1, curr, nums)
            curr.pop()
