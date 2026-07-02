class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list)
        visited = set()
        stack = set()

        for a,b in prerequisites:
            courses[b].append(a)

        def dfs(course):
            if course in stack:
                return False
            if course in visited:
                return True
            
            stack.add(course)
            
            for nei in courses[course]:
                if not dfs(nei):
                    return False

            visited.add(course)
            stack.remove(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
        
