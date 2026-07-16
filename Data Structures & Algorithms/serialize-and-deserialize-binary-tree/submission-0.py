# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "N"
        st = ""
        q = deque([root])

        while q:
            node = q.popleft()
            if node =="N":
                st += "N,"
            else:
                st += str(node.val) + ","

                if node.left:
                    q.append(node.left)
                else:
                    q.append("N")

                if node.right:
                    q.append(node.right)
                else:
                    q.append("N")
                
        return st

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data[0] =="N":
            return None
        data= data.split(',')
        data.pop()

        root = TreeNode(int(data[0]))
        q = deque([root])
        i = 0 
        while q:
            node = q.popleft()

            idx = (i+1) *2
            if data[idx-1] != "N":
                left = TreeNode(int(data[idx-1]))
                node.left = left
                q.append(left)

            if data[idx] != "N":
                right = TreeNode(int(data[idx]))
                node.right = right
                q.append(right)

            i+=1
        return root





# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))