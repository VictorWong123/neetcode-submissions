class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i in nums:
            if target-i in mp:
                return [index for index, value in enumerate(nums) if value == target-i or value==i]

            mp[i] = target-i


        