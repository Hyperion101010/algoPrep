class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        temp_stk = deque([])
        ans = [0 for _ in range(len(temperatures))]

        """
            The trick to solving this question is using monotonic stack.
            We put each temperature into stack and then fetch it out if the stack head is lesser than current temperature.
            If head is lesser that means we need to record this past temperature with the days that it will remain.
            This way we continue and get the final result.

            An interesting point about computing the time complexity of this solution is.
            We have stack and we append in stack only once for each temperature.
            So in worse case the stack will have N elements.
            Now for these N elements we will only get total N pops cause more than that is not possible.
            So N and N in worse case = 2 N
            Thus, O(N) is the time complexity.
        """

        for each_temp_idx in range(len(temperatures)):
            each_temp = temperatures[each_temp_idx]

            while len(temp_stk) > 0 and temp_stk[-1][0] < each_temp:
                obj = temp_stk.pop()
                past_temp, idx = obj[0], obj[1]
                ans[idx] = each_temp_idx - idx
            
            temp_stk.append([each_temp, each_temp_idx])

        return ans
