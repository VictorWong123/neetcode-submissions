class Solution:
    def reverse(self, x: int) -> int:
        res = int(str(abs(x))[::-1])

        if x<0:
            res *=-1

        if res <= -1 * (2**31) or res >= 2**31-1:
            return 0 

        return res

        return res