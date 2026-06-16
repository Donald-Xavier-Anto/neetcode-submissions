# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        cnt = dict()
        n = len(inorder)
        for i in range(0, n):
            cnt[inorder[i]] = i
        j = 0
        def dfs(l, r):
            if l>r:
                return None
            nonlocal j
            val = preorder[j]
            root = TreeNode(val)
            j += 1
            root.left = dfs(l, cnt[val]-1)
            root.right = dfs(cnt[val]+1, r)

            return root
        return dfs(0, n-1)

        