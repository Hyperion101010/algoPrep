class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int sz = prices.size();
        int arr[100000] = {0};
        int mx = 0;

        // The better approach is, we can first calculate what all maximum elements are possible in future.
        // Then one by one we check it with future values and keep updating the max profit.

        for(int i = prices.size() - 1; i >= 0; i--){
            if(prices[i] > mx){
                mx = prices[i];
                arr[i] = mx;
            }else{
                arr[i] = mx;
            }
        }

        int mx2 = 0;
        for(int i =1; i< prices.size() ;i++){

            // check the difference with my current price and max price possible in future.
            // Thus we now get the max price and update it if required.
            // return the max price.
            int dif = arr[i] - prices[i-1];
            if(dif > mx2){
                mx2 = dif;
            }
        }
        return mx2;
    }
};
