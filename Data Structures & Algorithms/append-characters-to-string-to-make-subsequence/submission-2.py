class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n= len(t)
        res = n
        l = 0 
        count = 0 
        for r in range(len(s)):
            if l>=n:
                return 0 
            if s[r] == t[l]:
                count +=1
                l+=1

            res = min(res,n-count)

        return res