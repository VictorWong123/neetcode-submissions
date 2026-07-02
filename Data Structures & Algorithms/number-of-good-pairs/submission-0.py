class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashmap = {}
        res = 0 

        for i in nums:
            if i in hashmap:
                res += hashmap[i]

                hashmap[i] +=1 
            else:
                hashmap[i] =1

        return res