class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        for a,b in prerequisites:
            adj_list[b].append(a)
        
        order = []
        stack = set()
        visited = set()
        res = True
        def dfs(course):
            nonlocal res,order

            if not res:
                return False
            if course in stack:
                res = False
                return False
            if course in visited:
                return True

            stack.add(course)
            for nei in adj_list[course]:
                dfs(nei)
                
            order.append(course)
            stack.remove(course)
            visited.add(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return order[::-1]

        