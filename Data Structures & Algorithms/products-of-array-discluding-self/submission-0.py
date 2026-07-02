class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)): 
            if i == len(nums):
                ls= nums[:i]
            else:
                ls = nums[:i] + nums[i+1:]
            k = 1
            for j in ls:
                k*=j
            output.append(k)
        return output

