# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"

        l = self.serialize(root.left)
        r = self.serialize(root.right)
        return str(root.val) + "|" + l + "|" + r

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        ind = 0
        d = data.split("|")
        # print(data)
        def build(s):
            nonlocal ind
            if ind >= len(s):
                return None
            if s[ind]=="N":
                ind += 1
                return None
            root = TreeNode(int(d[ind]))
            ind += 1
            root.left = build(s)
            root.right = build(s)

            return root
        return build(d)
            


