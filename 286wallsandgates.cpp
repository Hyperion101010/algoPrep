/*
Backup solution
class Solution {
public:
    vector<vector<bool>> visited;
    vector<vector<double>> lkup;
    int m, n;
    double inf = 0;

    double traverse(int x, int y, vector<vector<int>>& rooms){
        if(x >=m || x < 0 || y >= n || y < 0){
            return inf;
        }
        if(visited[x][y]){
            return lkup[x][y];
        }
        if(rooms[x][y] == -1){
            visited[x][y] = true;
            lkup[x][y] = inf;
            return lkup[x][y];
        }
        if(rooms[x][y] == 0){
            lkup[x][y] = 0;
            visited[x][y] = true;
            return 0;
        }
        visited[x][y] = true;

        double lft = traverse(x-1, y, rooms);
        double rgt = traverse(x+1, y, rooms);
        double up = traverse(x, y+1, rooms);
        double dwn = traverse(x, y-1, rooms);
        double ans = min(lft, min(rgt, min(up, dwn)));

        if(ans == inf){
            lkup[x][y] = inf;
            return lkup[x][y];
        }
        visited[x][y] = true;
        lkup[x][y] = 1 + ans;
        return lkup[x][y];
    }

    void wallsAndGates(vector<vector<int>>& rooms) {
        inf = 2147483647;
        m = rooms.size();
        n = rooms[0].size();

        visited = vector<vector<bool>>(m, vector<bool>(n, false));
        lkup = vector<vector<double>>(m, vector<double>(n, inf));

        for(int i =0; i< m; i++){
            for(int j = 0; j<n; j++){
                double ans;
                if(rooms[i][j] == -1 || rooms[i][j] == 0){
                    continue;
                }
                if(rooms[i][j] == inf){
                    ans = traverse(i,j, rooms);
                    rooms[i][j] = ans;
                    visited = vector<vector<bool>>(m, vector<bool>(n, false));
                }
            }
        }
    }
};
*/
class Solution {
public:
    vector<vector<bool>> visited;
    int m, n;
    double inf = 0;

    vector<pair<int, int>> chk = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    bool is_outside(int x, int y){
        if(x >= m || y >= n || x < 0 || y < 0){
            return true;
        }
        return false;
    }

    void traverse(queue<pair<int, int>>& q, vector<vector<int>>& rooms){
        while(!q.empty()){
            pair<int, int> pos = q.front();
            q.pop();

            int str_x = pos.first;
            int str_y = pos.second;
            visited[str_x][str_y] = true;

            for(int i =0; i< 4; i++){
                int pos_x = chk[i].first;
                int pos_y = chk[i].second;

                if(!is_outside(str_x + pos_x, str_y + pos_y) && rooms[str_x + pos_x][str_y + pos_y] != -1){
                    if(!visited[str_x + pos_x][str_y + pos_y]){
                        q.push({str_x + pos_x, str_y + pos_y});
                        rooms[str_x + pos_x][str_y + pos_y] = min(1 + rooms[str_x][str_y], rooms[str_x + pos_x][str_y + pos_y]);
                    }
                }
            }
        }
    }

    void wallsAndGates(vector<vector<int>>& rooms) {
        inf = 2147483647;
        m = rooms.size();
        n = rooms[0].size();

        // The trick is to not start traversal from the pathways but from the gates.
        // When you perform a Breadth First Search from gates
        // Now add distance from current state, min of that to take minimum in order.
        // Before start of the traversal your queue should have all the gates in it.
        // This way you will make sure that gates will be the start point of traverse.

        visited = vector<vector<bool>>(m, vector<bool>(n, false));

        queue<pair<int, int>> q;

        for(int i =0; i< m; i++){
            for(int j = 0; j<n; j++){
                double ans;
                if(rooms[i][j] == 0){
                    q.push({i, j});
                }
            }
        }
        traverse(q, rooms);
    }
};
