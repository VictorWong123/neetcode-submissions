class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0 
        cons = False
        count = 0 
        for r in range(len(nums)):
            if nums[r] == 1:
                cons = True
            else:
                cons = False
                count = 0 
            if cons:
                count +=1
            res = max(res, count)

        return res