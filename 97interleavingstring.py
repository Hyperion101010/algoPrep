class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.lkup = []

        """
            We start with lookup as a 2D DP with None as uninitialised state.
            True and False for the respective states.

            The DP state is of s1 left string index and s2 right string index
            So dp[left_idx][right_idx] stores the computation from that index for string s3.
        """
        for i in range(len(s1)+1):
            self.lkup.append([None for _ in range(len(s2)+1)])
        
        if len(self.s1) + len(self.s2) != len(self.s3):
            return False
        
        return self.vst(0, 0, '', 0)

    def vst(self, left_idx, right_idx, curr_str, running_idx):
        if left_idx >= len(self.s1) and right_idx >= len(self.s2):
            if running_idx > len(self.s3):
                return False
            else:
                if len(self.s3) > 0 and curr_str != self.s3[running_idx - 1]:
                    return False
            return True

        """
            At every step we check if that particular character if it matches with the s3 character.
            If it does not match then we don't need to check further and mark it as False.
            if it matches then continue and check till the string end.
        """
        if len(curr_str) > 0:
            if curr_str != self.s3[running_idx-1]:
                return False

        if self.lkup[left_idx][right_idx] is not None:
            return self.lkup[left_idx][right_idx]

        if left_idx >= len(self.s1):
            self.lkup[left_idx][right_idx] = self.vst(left_idx, right_idx+1, self.s2[right_idx], running_idx + 1)
            return self.lkup[left_idx][right_idx]
        
        if right_idx >= len(self.s2):
            self.lkup[left_idx][right_idx] = self.vst(left_idx+1, right_idx, self.s1[left_idx], running_idx + 1)
            return self.lkup[left_idx][right_idx]

        self.lkup[left_idx][right_idx] = self.vst(left_idx+1, right_idx, self.s1[left_idx], running_idx + 1) or (self.vst(left_idx, right_idx+1, self.s2[right_idx], running_idx + 1))

        return self.lkup[left_idx][right_idx]
