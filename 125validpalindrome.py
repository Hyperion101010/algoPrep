class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = re.split(r'[^a-zA-Z0-9]', s)
        ss = [i.lower() for i in ss]
        st = "".join(ss)
        fst = 0
        snd = len(st) - 1
        #print(st)
        while len(st) > 0 and fst <= snd:
            if st[fst] == st[snd]:
                fst+=1
                snd-=1
            else:
                return False
        return True

