class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        fst = 0
        snd = len(numbers) - 1
        while fst < snd:
            if numbers[fst] + numbers[snd] == target:
                return [fst + 1, snd + 1]
                break
            # after comparing the left and right ends we know that the left edge is smaller one
            # we can increment left one and then see that we contribute towards the target sum
            # thus we end up checking all posibilities by moving from left and right sides both at a time.
            if numbers[fst] + numbers[snd] < target:
                fst +=1
            # we first start by comparing the left and right extreme of the array
            # now if left and right is already above the target then its no point in incrementing left end
            # cause left end is ascending so it'll increase the sum
            # thus we move right one towards right
            elif numbers[fst] + numbers[snd] > target:
                snd -=1
        return [0, 0]
