class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix)-1

        while low<=high:
            mid = (low+high)//2
            middle = matrix[mid]
            for i in middle:
                l, h = 0, len(middle)-1
                while l<=h:
                    mid2 = (l+h)//2
                    print(middle)
                    print(mid2)
                    if middle[mid2] == target:
                        return True
                    elif middle[mid2] < target:
                        l = mid2 + 1
                    else:
                        h = mid2 -1


            if middle[0] <target:
                low = mid +1

            else:
                high = mid-1

        return False

            


