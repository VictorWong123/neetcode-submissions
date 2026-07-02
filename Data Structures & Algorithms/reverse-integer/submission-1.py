class Solution:
    def reverse(self, x: int) -> int:
        MIN = -1*(2**31) 
        MAX = 2**31-1
        res = 0 

        while x !=0:
            digit = x %10 if x>0 else x%-10

            res = res * 10 + digit
            print(res)
            if res>MAX or res<MIN:
                return 0
            x = int(x/10)

        return res