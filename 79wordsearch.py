class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        lkup = []
        for i in range(len(board)):
            tmp = [False for j in range(len(board[i]))]
            lkup.append(tmp)

        self.r = len(lkup)
        self.c = len(lkup[0])
        self.str_ln = len(word)
        self.wd = word
        self.bd = board
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                t = self.chk(i, j, 0, lkup)
                if t:
                    return True
        
        return False

    def chk(self, indx_r, indx_c, str_idx, lkup):

        """
            Some bound checks for indexes to not allow entries beyond bounds.
        """
        if str_idx >= self.str_ln:
            return True
        if indx_r >= self.r or indx_c >= self.c or indx_r < 0 or indx_c < 0:
            return False

        """
            lkup[indx_r][indx_c] is True
            then this means that this node is already visited
            thus now we are going to again visit some word that we already computed.
            If we already computed this then we should not again visit this node.
            Thus return False since it is a repeatition of the earlier explored path.
        """
        if lkup[indx_r][indx_c] is True:
            return False
    
        """
            The base condition that we found something and we need to explore more of its surroundings.
            Then go ahead for next index positions and explore all of them.
            Thus we now will check all posibilities and report them.
        """
        if self.wd[str_idx] == self.bd[indx_r][indx_c]:
            lkup[indx_r][indx_c] = True
            a = self.chk(indx_r, indx_c + 1, str_idx + 1, lkup)
            if a:
                return True
            b = self.chk(indx_r + 1, indx_c, str_idx + 1, lkup)
            if b:
                return True
            c = self.chk(indx_r - 1, indx_c , str_idx + 1, lkup)
            if c:
                return True
            d = self.chk(indx_r, indx_c - 1, str_idx + 1, lkup)
            if d:
                return True

            """
                This check means that for this position of array,
                we didn't find any proper solution.
                Thus now say that it's not visited and let it be computed by some other index position.
            """
            lkup[indx_r][indx_c] = False
        return False
