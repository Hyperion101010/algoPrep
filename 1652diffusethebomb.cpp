class Solution {
public:
    vector<int> decrypt(vector<int>& code, int k) {
        vector<int> arr;

        if(k > 0){
            for(int i =0; i< code.size();i++){
                int sz = code.size();
                int t = (i+1)% sz;
                int tm = k;
                int sm = 0;
                while(tm != 0){
                    sm += code[t];
                    t = (t+1)%sz;
                    tm-=1;
                }
                arr.push_back(sm);
            }
        }else if(k < 0){
            int kk = -1*k;
            for(int i =0; i< code.size();i++){
                int sz = code.size();
                int t = ((i-1) + sz)% sz;
                int tm = kk;
                int sm = 0;
                while(tm != 0){
                    sm += code[t];

                    // for the real modulus you need to do; (index + size) mod (size)
                    t = ((t-1) + sz)%sz;
                    tm-=1;
                }
                arr.push_back(sm);
            }
        }else{
            for(int i =0; i< code.size(); i++){
                arr.push_back(0);
            }
        }
        return arr;
    }
};
