class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res, resLen = "", float('inf')
        window, t_map = {}, Counter(t)
        have, need = 0, len(t_map)
        l = 0 

        for r in range(len(s)):
            c = s[r]

            window[c] = window.get(c,0) +1

            if c in t_map and window[c]==t_map[c]:
                have+=1

            while have == need:
                ch = s[l]
                if len(s[l:r])<resLen:
                    resLen = r-l+1
                    res = s[l:r+1]

                window[ch] -=1
                if ch in t_map and window[ch]< t_map[ch]:
                    have -=1
                l+=1
            
        return "" if resLen == float('inf') else res
