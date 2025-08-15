class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
            Sol link - https://www.youtube.com/watch?v=NNcN5X1wsaw
            The crux of this problem is that,
            1. It can't be solved in greedy way by sorting the array 
            and then looking for amounts from lower order.
            2. It can't be solved in Brute force way.

            We see that let's say to make amount = 11 in a set of [1, 5, 6, 9]
            we can have many possibilities like 6 , 1, ,1 ..
            we can make 5, 1, 1..
            or we can have 9, 1, 1
            or 5,6

            So we choose 9 then its choosing how many less counts we can make remainder thats 2.
            So if we choose 5 then its choosing how to make 6
            So its like when we choose a coin we need to store or remember how to make other remainder.

            So it can be any number so we got to start from amount 0 to the real amount required.

            Also when selecting the coin we check if its greater than amount then we just break it.
        """

        # Initialize array with max coins count.
        dp = [10e9 for i in range(amount + 1)]

        # sort coins so that we can break in middle.
        coins = sorted(coins)

        if amount <= 0:
            return amount
        
        for i in range(amount + 1):
            j = 0

            # Default case, start of DP.
            if i == 0:
                dp[0] = 0
                continue
            
            # Run all possibilities to select coins from the set.
            # In selection keep updating minimum count found.
            while j < len(coins) and i >= coins[j]:
                dp[i] = min(dp[i], 1 + dp[i - coins[j]])
                j+=1

        # If amount still max then means no solution found.
        if dp[amount] == 10e9:
            return -1

        # Solution is found, return the answer.
        return dp[amount]
