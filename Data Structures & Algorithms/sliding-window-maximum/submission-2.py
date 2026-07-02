class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        for i in range(len(nums)-k+1):
            highest = nums[i]
            for j in range(i,i+k):
                highest = max(highest,nums[j])
            res.append(highest)
        return res

