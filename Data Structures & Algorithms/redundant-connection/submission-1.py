class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        n = len(edges)

        def dfs(node,par):
            if visited[node]==True:
                return True
            visited[node] = True

            for nei in adj_list[node]:
                if nei ==par:
                    continue
                if dfs(nei,node):
                    return True
            return False
        

        for e,v in edges:
            adj_list[e].append(v)
            adj_list[v].append(e)

            visited = [False]*(n+1)

            if dfs(e,-1):
                return [e,v]

        return []

