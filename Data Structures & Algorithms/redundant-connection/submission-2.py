class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        cycle = set()
        cycle_start = -1
        n = len(edges)
        adj_list = defaultdict(list)
        visited = [False]*(n+1)

        for f,t in edges:
            adj_list[f].append(t)
            adj_list[t].append(f)

        def dfs(node, par):
            nonlocal cycle_start
            if visited[node]:
                cycle_start = node
                return True

            visited[node] = True
            for nei in adj_list[node]:
                if nei == par:
                    continue
                if dfs(nei, node):
                    if cycle_start != -1:
                        cycle.add(node)
                    if cycle_start == node:
                        cycle_start = -1

                    return True
            return False

        dfs(1,-1)    
        for f,t in edges[::-1]:
            if f in cycle and t in cycle:
                return [f,t]
        return []