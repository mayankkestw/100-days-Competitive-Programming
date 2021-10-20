#include<bits/stdc++.h>

using namespace std;

class Solution
{
    public:
	vector<int>bfsOfGraph(int V, vector<int> adj[])
	{
	    queue<int> q;
	    q.push(0);
	    vector<bool> vis(V, false);
	    vis[0] = true;
	    int current;
	    vector<int> bfs;
	    bfs.push_back(0);
	    while(!q.empty()) {
	        current = q.front();
	        q.pop();
	        for(int u: adj[current]) {
	            if(!vis[u]) {
	                q.push(u);
	                bfs.push_back(u);
	                vis[u] = true;
	            }
	        }
	    }
	    
	return bfs;
	    
	}
};

int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int V, E;
    	cin >> V >> E;

    	vector<int> adj[V];

    	for(int i = 0; i < E; i++)
    	{
    		int u, v;
    		cin >> u >> v;
    		adj[u].push_back(v);
    	}
        
        Solution obj;
        vector<int>ans=obj.bfsOfGraph(V, adj);
        for(int i=0;i<ans.size();i++){
        	cout<<ans[i]<<" ";
        }
        cout<<endl;
	}
	return 0;
}