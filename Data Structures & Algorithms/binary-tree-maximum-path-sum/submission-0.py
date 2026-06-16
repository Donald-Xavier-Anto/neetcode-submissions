# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        mx_path = float("-infinity")
        def dfs(root):
            if not root:
                return 0
            nonlocal mx_path
            l = dfs(root.left)
            r = dfs(root.right)
            mx_path = max(mx_path, l + r + root.val)
            return max(max(l,r)+root.val, 0)
        dfs(root)
        return mx_path
        