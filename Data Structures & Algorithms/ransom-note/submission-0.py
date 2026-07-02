class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = Counter(magazine)
        hashmap2 = Counter(ransomNote)

        for key,val in hashmap2.items():
            if key not in hashmap or hashmap[key]<val:
                return False

        return True