class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i,sol):
            nonlocal res
            if sum(sol)==target:
                res.append(sol[:])
                return 
            if i>= len(nums) or sum(sol)>target:
                return 
            
            backtrack(i+1,sol)

            sol.append(nums[i])
            backtrack(i,sol)
            sol.pop()

        backtrack(0,[])
        return res