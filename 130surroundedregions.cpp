class Solution {
public:
    int m,n;
    vector<vector<bool>> visited;
    vector<vector<bool>> marked;
    vector<vector<int>> chk = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    
    void check(int x, int y, vector<vector<char>>& board){
        if(x > m || y > n || x < 0 || y < 0){
            return;
        }
        if(board[x][y] == 'X'){
            return;
        }
        if(visited[x][y]){
            return;
        }
        visited[x][y] = true;
        marked[x][y] = true;
        for(int i = 0; i < 4 ; i++){
            check(x + chk[i][0], y + chk[i][1], board);
        }
        return;
    }

    void solve(vector<vector<char>>& board) {
        m = board.size() - 1;
        n = board[0].size() - 1;

        // Only traverse from edges, the neighbors that are possible to be visited mark them.
        // Then just make those 'O' points as 'X' which were not able to be visited.
        // Thus it will work.
        visited = vector(m + 1, vector<bool>(n + 1, false));
        marked = vector(m + 1, vector<bool>(n + 1, false));

        for(int i = 0; i <= m; i++){
            for(int j = 0; j <= n; j++){
                if((i == 0 || j == 0 || i == m || j == n) && board[i][j] == 'O'){
                    check(i, j, board);
                }
            }
        }

        for(int i = 0; i <= m; i++){
            for(int j = 0; j <= n; j++){
                if(!marked[i][j] && board[i][j] == 'O'){
                    board[i][j] = 'X';
                }
            }
        }

        return;
    }
};

