class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list= defaultdict(list)

        for f,t in edges:
            adj_list[f].append(t)
            adj_list[t].append(f)

        seen = set()


        def dfs(node, parent):
            seen.add(node)

            for nei in adj_list[node]:
                if nei == parent:
                    continue
                if nei in seen: 
                    return False #cycle

                if not dfs(nei,node):
                    return False

            return True



        if not dfs(0,-1):
            return False

        return len(seen)==n #connected
