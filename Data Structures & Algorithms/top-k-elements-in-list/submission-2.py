class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] +=1
        res = []
        print(hashmap)
        while k>0:
            val = max(hashmap, key=hashmap.get)
            res.append(val)
            del hashmap[val]
            k-=1
        return res