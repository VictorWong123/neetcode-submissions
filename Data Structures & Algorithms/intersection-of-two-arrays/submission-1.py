class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sett = set(nums1)
        res = []
        for i in nums2:
            if i in sett:
                res.append(i)
        return list(set(res))