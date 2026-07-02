class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(i,sol):
            if i==len(digits):
                res.append(sol)
                return
            for c in my_dict[int(digits[i])]:
                dfs(i + 1, sol + c)

        if not digits:
            return []
        my_dict = {2:"abc", 3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        res = []
        
        dfs(0,"")

        return res


