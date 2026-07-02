class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def dfs(i,sol):
            if i == n:
                res.append(sol[:])
                return
            
            for j in range(i,n):
                nums[j],nums[i] = nums[i], nums[j]
                dfs(i+1,nums)
                nums[j],nums[i] = nums[i], nums[j]



        dfs(0,[])
        return res