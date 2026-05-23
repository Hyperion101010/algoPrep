class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
            We keep a 2D DP for storing the states of computation for
            each amount and if we start from the amount how much ways we will make.
            So dp is dp[amount][coin_lst_size]
        """
        self.lkup = []
        self.ln = len(coins)
        self.coins = sorted(coins)
        for i in range(amount + 1):
            self.lkup.append([-1 for _ in range(len(coins))])
        
        return self.vst(amount, 0)

    
    def vst(self, amount, idx):
        if idx >= self.ln:
            return 0
        
        if amount == 0:
            return 1
        
        if self.lkup[amount][idx] > -1:
            return self.lkup[amount][idx]
        
        if self.coins[idx] > amount:
            return 0
        
        """
            For each coin either we select it in counting and substract the amount
            or start with the new coin and fresh amount to compute.
        """
        self.lkup[amount][idx] = self.vst(amount - self.coins[idx], idx) + self.vst(amount, idx+1)

        return self.lkup[amount][idx]
