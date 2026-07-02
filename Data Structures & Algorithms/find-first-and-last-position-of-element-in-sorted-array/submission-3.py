class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        l = 0 
        r = len(nums)-1
        res = []
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                x  = mid -1
                y = mid +1
                while 0<=x and nums[x] == target:
                    x-=1
                while y<=r and nums[y] == target:
                    y+=1
                return [x+1,y-1]
            elif nums[mid]< target:
                l = mid + 1
            else:
                r = mid -1 

        return [-1,-1] 