class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ls = [i for i in range(1,n+1)]
        res = []
        def backtrack(i,sol):
            if len(sol) ==k:
                res.append(sol[:])
                return 
            if i ==n:
                return
                        
            sol.append(ls[i])
            backtrack(i+1,sol)
            sol.pop()
            
            backtrack(i+1,sol)

        backtrack(0,[])
        return res
