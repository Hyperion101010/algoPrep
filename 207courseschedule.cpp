class Solution {
public:
    vector<vector<int>> graph;
    vector<bool> visited;
    vector<int> indegree;
    int cnt = 0;

    void traverse(){
        queue<int> q;

        for(int i =0;i< indegree.size();i++){
            if(indegree[i] == 0){
                q.push(i);
            }
        }

        while(!q.empty()){
            int course = q.front();
            q.pop();
            cnt+=1;

            for(int i =0; i < graph[course].size() ; i++){
                int ele = graph[course][i];

                indegree[ele]-=1;

                if(indegree[ele] == 0){
                    q.push(ele);

                }
            }
        }
    }

    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        graph.resize(numCourses);
        visited = vector(numCourses, false);
        indegree = vector(numCourses, 0);

        // This is a typical implementatoin of Kahn's algorithm
        // We maintain a indegree lookup where we count
        // how many edges each point has.
        // Then we try to traverse from those edges to the end.
        // Thus we then get a topological sort.

        for(int i = 0; i < prerequisites.size(); i++){
            int lft = prerequisites[i][0];
            int rgt = prerequisites[i][1];
            graph[lft].push_back(rgt);
        }

        for(int i = 0; i < graph.size() ;i++){
            for(int j = 0; j < graph[i].size(); j++){
                indegree[graph[i][j]]+=1;
            }
        }

        traverse();

        if(cnt == numCourses || prerequisites.size() == 0){
            return true;
        }
        
        return false;
    }
};
