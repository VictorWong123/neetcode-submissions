class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        up, down, res = 1,1,1

        for i in range(1,len(arr)):
            if arr[i-1]>arr[i]:
                up = down + 1
                down = 1
            elif arr[i-1]<arr[i]:
                down = up + 1
                up = 1

            else:
                down = 1
                up = 1
            res = max(res,up,down)
            
        return res