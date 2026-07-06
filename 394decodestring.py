class Solution:
    def is_int(self, s):
        nm = ord(s) - ord('0')
        if 0 <= nm <= 9:
            return nm
        return -1
    
    def is_alpha(self, s):
        return 0 <= ord(s) - ord('a') <= 25


    def decodeString(self, s: str) -> str:
        nm = 0
        st = ''

        nm_stack = deque([])
        str_stack = deque([])

        """
            The solution to this problem is we will use 2 stacks.
            First stack we will use to keep track of numbers we have encountered.
            Second stack we will use to keep track of the strings we encountered before [] began.
            Now we take the string before and perform past_string + times*curr_string for the answer.
            Then we return the total answer.
        """


        for each_idx in range(len(s)):
            ch = s[each_idx]
            curr_nm = self.is_int(ch)

            if curr_nm != -1:
                nm = 10*nm + curr_nm
            
            if self.is_alpha(ch):
                st = st + ch

            if ch == '[':
                nm_stack.append(nm)
                str_stack.append(st)
                st = ''
                nm = 0
            if ch == ']':
                times = nm_stack.pop()
                if len(str_stack) > 0:
                    tmp_st = str_stack.pop()
                    st = tmp_st + st*times
                else:
                    st = st*times

        return st
