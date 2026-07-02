class Solution:
    def isHappy(self, n: int) -> bool:
        sett = set()
        sett.add(n)
        while n!=1:
            st = 0
            for i in str(n):
                st+= int(i)**2

            n = st

            if n in sett:
                return False
            else:
                sett.add(n)
        return True