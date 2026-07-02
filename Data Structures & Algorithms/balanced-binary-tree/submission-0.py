# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]
            lheight = dfs(root.left)
            rheight = dfs(root.right)

            balanced = lheight[0] and rheight[0] and abs(lheight[1]-rheight[1])<=1
            return [balanced, max(lheight[1],rheight[1])+1]

        return dfs(root)[0]
