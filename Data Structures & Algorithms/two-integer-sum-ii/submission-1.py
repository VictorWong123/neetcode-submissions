class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0 
        r = len(numbers)-1

        while l<r:
            x = numbers[l]
            y = numbers[r]
            if x+y == target:
                return [l+1,r+1]
            elif x+y< target:
                if l<r:
                    l+=1
                else:
                    r-=1
            else:
                if l<r:
                    r-=1
                else: 
                    l+=1