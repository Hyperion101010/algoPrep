class Solution {
public:
    vector<vector<int>> ans;
    vector<vector<int>> chk = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
    vector<vector<bool>> visited;

    int m, n;

    void traverse(int prev, int x, int y, vector<vector<int>>& ocean,vector<vector<int>>& heights){
        if(x > m || y > n || x < 0 || y < 0){
            return;
        }
        if(visited[x][y]){
            return;
        }
        if(ocean[x][y] >= 1){
            return;
        }

        if(heights[x][y] >= prev){
            // Mark it visited only if you can visit it.
            // Now since we can move ahead, now we can mark it as visited.
            // And now visit other neighbors.
            visited[x][y] = true;
            ocean[x][y] = 1;
            for(int i=0; i < 4; i++){
                traverse(heights[x][y], x + chk[i][0], y + chk[i][1], ocean, heights);
            }
        }else{
            return;
        }
        return;
    }

    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        m = heights.size() - 1;
        n = heights[0].size() - 1;

        // The trick to solve this problem is to check from surrounding bounaries.
        // Start from each boundary and visit all nodes greater than itself.
        // Now in this way maintain two maps, one for each ocean - atlantic and pacific.
        // In this manner we can know which one is valid.
        // Put everything in a vector and return it.
        vector<vector<int>> pacific, atlantic;

        pacific = vector(m + 1, vector<int>(n + 1, -1));
        atlantic = vector(m + 1, vector<int>(n + 1, -1));

        for(int i = 0; i <= m; i++){
            visited = vector(m + 1, vector<bool>(n + 1, false));
            traverse(-1, i, 0, pacific, heights);
        }
        for(int i = 0; i <= n; i++){
            visited = vector(m + 1, vector<bool>(n + 1, false));
            traverse(-1, 0, i, pacific, heights);
        }
        for(int i = 0; i <= n; i++){
            visited = vector(m + 1, vector<bool>(n + 1, false));
            traverse(-1, m, i, atlantic, heights);
        }
        for(int i = 0; i <= m; i++){
            visited = vector(m + 1, vector<bool>(n + 1, false));
            traverse(-1, i, n, atlantic, heights);
        }

        for(int i =0; i <= m; i++){
            for(int j = 0; j <= n; j++){
                if(atlantic[i][j] == 1 && pacific[i][j] == 1){
                    vector<int> tmp;
                    tmp.push_back(i);
                    tmp.push_back(j);
                    ans.push_back(tmp);
                }
            }
        }
        return ans;
    }
};
