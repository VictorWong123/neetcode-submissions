# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0 
        def dfs(root,st):
            nonlocal total
            if not root:
                return 0
            st += str(root.val)

            if not root.left and not root.right:
                total += int(st)
                return

            return dfs(root.left,st) or dfs(root.right,st)
        
        dfs(root,"")
        return total