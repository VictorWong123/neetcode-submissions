# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        q = deque()
        q.append(root)

        total = 0 

        while q:
            for i in range(len(q)):
                x = q.popleft()
                if low<=x.val<=high:
                    total += x.val
                    
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
        return total