# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root, mx):
        if not root:
            return 0
        l = self.helper(root.left, max(mx, root.val))
        r = self.helper(root.right, max(mx, root.val))
        if root.val >= mx:
            return l + r + 1
        return l + r

    def goodNodes(self, root: TreeNode) -> int:
        return self.helper(root, -101)
        
        