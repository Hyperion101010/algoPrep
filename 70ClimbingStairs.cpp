class Solution {
public:
    int driver(int n, vector<int> &lkup){
        if(n < 1){
            return 0;
        }
        if(lkup[n]!=-1){
            return lkup[n];
        }

        // Call the 2 distinct ways of combining results.
        // driver(n-1, lkup) ---> means creating n-1 number with adding 1 into its sum.
        // driver(n-2, lkup) ---> means creating n-2 number with adding 2 into its sum.
        // Thus, addition of both of these results will give you the final answer.
        lkup[n] = driver(n-1, lkup) + driver(n-2, lkup);
        return lkup[n];
    }

    // The problem is breaking down the computations into sub problems
    // Let's consider making 3
    // To make 3
    // we do as dp[n] = dp[n-2] + dp[n-1]
    // dp[n-2] means choosing creating a number n-2 in one way and keeping 2 as its constituent
    // dp[n-1] means choosing creating a number n-1 in one way and keeping 1 as its constituent
    //      3 |
    //.       |
    // (2, 1).  + (1, 2) = 2 + 1 (1 comes from ( (-1, 2) and (0, 1) = 1 ))
    //    |
    //.  (0, 2). + (1,1) = 2
    int climbStairs(int n) {
        vector<int> lkup(46, -1);

        // precompute base cases for our DP.
        lkup[0] = 0;
        lkup[1] = 1;
        lkup[2] = 2;

        return driver(n, lkup);
    }
};
