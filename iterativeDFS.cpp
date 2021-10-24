#include<bits/stdc++.h>
using namespace std;

class Graph
{
    int V;  
    list<int> *adj; 
public:
    Graph(int V); 
    void addEdge(int v, int w); 
    void DFS(int s); 
};
 
Graph::Graph(int V)
{
    this->V = V;
    adj = new list<int>[V];
}
 
void Graph::addEdge(int v, int w)
{
    adj[v].push_back(w);
}
 
void Graph::DFS(int s)
{
    vector<bool> visited(V, false);
 
    stack<int> stack;
 
    stack.push(s);
 
    while (!stack.empty())
    {
        int s = stack.top();
        stack.pop();
        
        if (!visited[s])
        {
            cout << s << " ";
            visited[s] = true;
        }
 
        for (auto i = adj[s].begin(); i != adj[s].end(); ++i)
            if (!visited[*i])
                stack.push(*i);
    }
}
 
int main()
{
    Graph g(5); 
    g.addEdge(1, 0);
    g.addEdge(0, 2);
    g.addEdge(2, 1);
    g.addEdge(0, 3);
    g.addEdge(1, 4);
 
    cout << "Following is Depth First Traversal\n";
    g.DFS(0);
 
    return 0;
}