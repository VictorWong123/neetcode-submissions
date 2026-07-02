class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        greedy = nums[0]
        count = 0 

        for i in nums:            
            if count <0:
                count = 0 
            count+=i
            greedy = max(greedy,count)
        return greedy