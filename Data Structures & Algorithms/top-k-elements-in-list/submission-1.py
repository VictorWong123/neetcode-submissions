class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] +=1
        print(hashmap)
        output = []

        for i in range(k):
            high = max(hashmap,key=hashmap.get)
            output.append(high)
            hashmap[high] = 0

        return output



    
