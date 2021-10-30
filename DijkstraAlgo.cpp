#include<bits/stdc++.h>
using namespace std;

class Solution
{
	public:
      vector<int> dijkstra(int V, vector<vector<int>> adj[], int S) {
        vector<int> dist(V + 1, INT_MAX);
        dist[S] = 0;
        vector<bool> vis(V, false);
        for (int a = 0; a < V; a++) {
            int x = S;
            int m = INT_MAX;
            for (int j = 0; j < V; j++)
                if (!vis[j] && dist[j] < m)
                    m = dist[j], x = j;

            vis[x] = true;
            for (auto i : adj[x]) {
                if (!vis[i[0]] && dist[x] + i[1] < dist[i[0]])
                    dist[i[0]] = dist[x] + i[1];
            }
        }
        return dist;
    }
};


int main()
{
    int t;
    cin >> t;
    while (t--) {
        int V, E;
        cin >> V >> E;
        vector<vector<int>> adj[V];
        int i=0;
        while (i++<E) {
            int u, v, w;
            cin >> u >> v >> w;
            vector<int> t1,t2;
            t1.push_back(v);
            t1.push_back(w);
            adj[u].push_back(t1);
            t2.push_back(u);
            t2.push_back(w);
            adj[v].push_back(t2);
        }
        int S;
        cin>>S;
        
        Solution obj;
    	vector<int> res = obj.dijkstra(V, adj, S);
    	
    	for(int i=0; i<V; i++)
    	    cout<<res[i]<<" ";
    	cout<<endl;
    }

    return 0;
}