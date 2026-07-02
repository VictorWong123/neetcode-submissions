class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for i in strs: 
            count = ''.join(sorted(i))
            hashmap[tuple(count)].append(i)
        print(hashmap)
        return hashmap.values()
