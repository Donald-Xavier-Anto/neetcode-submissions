# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root):
        if not root:
            return (0, 0)

        l, a = self.helper(root.left)
        r, b = self.helper(root.right)

        return (max(l,r)+1, max(l+r+1, a, b))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.helper(root)[1] - 1
        