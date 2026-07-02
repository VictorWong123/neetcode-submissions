# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        total = [root.val]
        def dfs(root):
            nonlocal total
            if not root:
                return 0 

            right = dfs(root.right) 
            left = dfs(root.left)

            right = max(right, 0)
            left = max(left,0)
            total[0] = max(total[0],right+left+ root.val)

            return root.val + max(left,right)




        dfs(root)
        return total[0]