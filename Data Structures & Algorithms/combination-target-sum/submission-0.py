class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        def backtrack(i, sol,total):
            print(total)
            if i >= n or total>target:
                return
            if total == target:
                res.append(sol[:])
                return
            
            backtrack(i+1,sol,total)

            sol.append(nums[i])
            backtrack(i,sol,total+nums[i])
            sol.pop()

        backtrack(0,[],0)
        return res
