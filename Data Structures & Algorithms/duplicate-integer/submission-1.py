class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ls = []
        for i in nums: 
            if i in ls:
                return True
            ls.append(i)
        return False
            
