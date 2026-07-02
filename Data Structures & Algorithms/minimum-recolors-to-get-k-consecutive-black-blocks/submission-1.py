class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        hashmap = {}

        for i in range(k):
            block = blocks[i]
            if block not in hashmap:
                hashmap[block] =1
            else:
                hashmap[block] +=1
        if "W" not in hashmap:
            return 0
        n = len(blocks)
        l = 0
        res = hashmap["W"]
        for i in range(k,n):
            hashmap[blocks[l]]-=1
            hashmap[blocks[i]] +=1
            res = min(res,hashmap["W"])

            l+=1
        
        return res


