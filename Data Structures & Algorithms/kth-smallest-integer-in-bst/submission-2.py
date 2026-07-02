# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0 
        res = 0 
        def in_order(root):
            if not root:
                return 

            nonlocal count
            nonlocal res

            in_order(root.left)

            count+=1
            if count==k:
                res = root.val

            in_order(root.right)
        in_order(root)
            
        return res

            
            