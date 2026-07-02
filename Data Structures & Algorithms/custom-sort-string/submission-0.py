class Solution:
    def customSortString(self, order: str, s: str) -> str:
        sett = Counter(s)
        res = ""

        for i in order:
            if i in sett:
                res += (i *sett[i])

                del sett[i]

        for key,val in sett.items():
            res += (key*val)
        return res 

        