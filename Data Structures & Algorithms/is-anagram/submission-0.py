class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}
        if len(s) != len(t):
            return False
            
        for i in range(len(s)):
            if s[i] not in s_map:
                s_map[s[i]] = 1
            else:             
                s_map[s[i]]+=1

            if t[i] not in t_map:
                t_map[t[i]] = 1
            else:            
                t_map[t[i]]+=1
        return s_map == t_map

