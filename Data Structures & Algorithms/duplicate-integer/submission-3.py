class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers = []
        for n in nums:
            if n not in numbers:
                numbers.append(n)
            else:
                return True

        return False