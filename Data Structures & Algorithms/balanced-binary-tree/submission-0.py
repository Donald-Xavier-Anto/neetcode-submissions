# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root):
        if not root:
            return (0, True)

        l, bl = self.helper(root.left)
        r, br = self.helper(root.right)

        if not bl or not br:
            return (0, False)
        
        if abs(l-r)>1:
            return (0, False)

        return (max(l,r)+1, True)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root)[1]        