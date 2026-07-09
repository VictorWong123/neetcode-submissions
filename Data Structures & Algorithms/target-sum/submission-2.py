class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = 0 

        def backtrack(i,total):
            nonlocal res
            if i ==len(nums) and total == target:
                res+=1
                return

            if i>=len(nums):
                return 
            

            total += nums[i] 
            backtrack(i+1, total)
            total -= nums[i]

            total -= nums[i]
            backtrack(i+1, total)
            total += nums[i]
            
        backtrack(0,0)
        return res


