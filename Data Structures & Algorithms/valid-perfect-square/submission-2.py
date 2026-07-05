class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num ==1 or num ==0:
            return True
        return int(num**(1/2)) == num**(1/2)