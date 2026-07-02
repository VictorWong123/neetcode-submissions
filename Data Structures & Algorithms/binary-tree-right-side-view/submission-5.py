# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        def bfs(root):
            res = []
            queue = deque([root])
            while queue:
                n= len(queue)
                for i in range(n):
                    x = queue.popleft()

                    if i ==n-1:
                        res.append(x.val)

                    if x.left:
                        queue.append(x.left)
                    if x.right:
                        queue.append(x.right)
            return res

        return bfs(root)

