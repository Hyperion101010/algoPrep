class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_nm = []

        # We maintain a vector pair type representation in our python.
        # We first sort it for better finding, then we return the pairs.
        # Same as two sum sorting but this one we track indices through extra space.
        for i in range(len(nums)):
            new_nm.append([nums[i], i])

        new_nm = sorted(new_nm)
        fst = 0
        snd = len(nums) - 1
        while fst < snd:
            if new_nm[fst][0] + new_nm[snd][0] == target:
                return [new_nm[fst][1], new_nm[snd][1]]
            elif new_nm[fst][0] + new_nm[snd][0] < target:
                fst += 1
            else:
                snd -= 1
        return [new_nm[fst][1], new_nm[snd][1]]
