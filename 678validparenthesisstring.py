class Solution:
    def checkValidString(self, s: str) -> bool:
        # If even then on both side we need either equal or equal deletions or just one star.
        # If odd then check if middle element is *, if not star then we need to check something else.
        self.end_idx = len(s) - 1
        self.s = s

        """
            The problem has input constriants of 100 as the string length.
            So we will be using a DP solution where we maintain the total_braces.
            It operates as a stack so for each left_bracket we push in stack so total_braces + 1
            If we get right_bracket then we pop out of stack so total_braces - 1.
            For the position of index and total_braces of the function call.
            Then now we store the result and thus and at the end of index we compute if total_braces is < 0.
            Then we return False if total_braces < 0 and True if total_braces == 0.
            Complexity = n^2?
        """

        self.dp = []
        for i in range(101):
            self.dp.append([None for i in range(101)])

        if len(s) == 1 and s[0] != '*':
            return False

        return self.cnt(0, 0)

    def cnt(self, total_braces, idx):
        if idx > self.end_idx:            
            if total_braces == 0:
                return True
            
            return False
        
        if total_braces < 0:
            return False

        if self.dp[total_braces][idx] is not None:
            return self.dp[total_braces][idx]
        
        if self.s[idx] == '*':
            self.dp[total_braces][idx] = self.cnt(total_braces - 1, idx + 1) or self.cnt(total_braces + 1, idx + 1) or self.cnt(total_braces, idx + 1)
        
        if self.s[idx] == '(':
            self.dp[total_braces][idx] = self.cnt(total_braces + 1, idx + 1)
        
        if self.s[idx] == ')':
            self.dp[total_braces][idx] = self.cnt(total_braces - 1, idx + 1)
            return self.dp[total_braces][idx]
        
        return self.dp[total_braces][idx]
