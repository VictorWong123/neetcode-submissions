# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque()
        if not root:
            return []
    
        queue= deque([root])

        while queue:
            temp = []
            for i in range(len(queue)):
                x= queue.popleft()
                if x.left:
                    queue.append(x.left)
                if x.right:
                    queue.append(x.right)

                temp.append(x.val)
            res.append(temp)
        return res



        