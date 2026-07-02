class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = nums[0]
        print(nums)
        while l<=r:
            print(l,r)
            print(res)
            mid = (l+r)//2
            if nums[mid]< res:
                res = nums[mid]
                r = mid -1
            else:
                l = mid +1


        return res
