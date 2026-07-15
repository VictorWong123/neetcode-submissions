class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        prefix = [0] * (n+1)
        vowels = "aeiou"
        total = 0
        for i in range(n):
            word = words[i]
            if word[0] in vowels and word[-1] in vowels:
                total +=1
            prefix[i+1] = total

        res = []
        for start, end in queries:
            res.append(prefix[end+1]-prefix[start])
        return res

