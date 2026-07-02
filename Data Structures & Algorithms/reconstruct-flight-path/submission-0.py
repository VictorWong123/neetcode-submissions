class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = defaultdict(list)

        tickets.sort()
        for f,t in tickets:
            adj_list[f].append(t)

        res = ["JFK"]

        def dfs(i):
            if len(res) == len(tickets)+1:
                return True

            if i not in adj_list:
                return False
            
            nei = list(adj_list[i])

            for idx,v in enumerate(nei):
                adj_list[i].pop(idx)
                res.append(v)
                if dfs(v):
                    return True
                adj_list[i].insert(idx,v)
                res.pop()

            return False
        dfs("JFK")

        return res