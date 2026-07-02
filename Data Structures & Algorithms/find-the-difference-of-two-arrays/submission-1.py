class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        sett = set(nums1)
        s = set(nums2)

        res =[[],[]]
        for i in nums1:
            if i not in s:
                res[0].append(i)
                s.add(i)
        
        for i in nums2:
            if i not in sett:
                res[1].append(i)
                sett.add(i)

        return res