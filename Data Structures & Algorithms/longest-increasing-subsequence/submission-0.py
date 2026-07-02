class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = n * [1]
        
        def dfs(i):
            if i >= n:
                return 0 
            
            res = 1
            for j in range(i+1,n):
                if nums[j]> nums[i]:
                    res = max(res, 1+dfs(j))
            dp[i] = res
            return res
            
        return max(dfs(i) for i in range(n))
        


