class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        curr_max = nums[0]
        curr_min = nums[0]
        res = nums[0]

        for i in range(1,n):
            options = (nums[i],nums[i]*curr_max,nums[i]*curr_min)
            curr_max = max(options)
            curr_min = min(options)
            res = max(curr_max,res)
        
        return res