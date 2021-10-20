import java.util.*;
import java.lang.*;
import java.io.*;
class DFS
{
    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine().trim());
        while(T-->0)
        {
            String[] s = br.readLine().trim().split(" ");
            int V = Integer.parseInt(s[0]);
            int E = Integer.parseInt(s[1]);
            ArrayList<ArrayList<Integer>>adj = new ArrayList<ArrayList<Integer>>();
            for(int i = 0; i < V; i++)
                adj.add(new ArrayList<Integer>());
            for(int i = 0; i < E; i++){
                String[] S = br.readLine().trim().split(" ");
                int u = Integer.parseInt(S[0]);
                int v = Integer.parseInt(S[1]);
                adj.get(u).add(v);
                adj.get(v).add(u);
            }
            Solution obj = new Solution();
            ArrayList<Integer>ans = obj.dfsOfGraph(V, adj);
            for (int i =0 ;i < ans.size (); i++) 
                System.out.print (ans.get (i) + " ");
            System.out.println();
        }
    }
}


class Solution
{
    public ArrayList<Integer> dfsOfGraph(int V, ArrayList<ArrayList<Integer>> adj)
    {
        // Code here
        ArrayList<Integer> al = new ArrayList<Integer>();
        boolean vis[] = new boolean[V];
        dfs(0,adj,al,vis);
        return al;
    }
    
    public void dfs(int i, ArrayList<ArrayList<Integer>> adj,ArrayList<Integer> al, boolean[] vis){
        if(vis[i] == true)
        return;
        vis[i] = true;
        al.add(i);
        for(int j=0;j<adj.get(i).size();j++){
            dfs(adj.get(i).get(j),adj,al,vis);
        }
        
    }
}