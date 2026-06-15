# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = -1
        def dfs(root, t):
            if not root:
                return 0
            nonlocal ans
            l = dfs(root.left, t)
            if (t + l) == k-1:
                ans = root.val
            r = dfs(root.right, t + l + 1)
            return l + r + 1
        dfs(root, 0)
        return ans

        