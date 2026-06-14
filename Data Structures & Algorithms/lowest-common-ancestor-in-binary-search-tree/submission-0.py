# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def printer(self, t):
    #     print(t)
    #     return t

    def helper(self, root, p, q):
        if not root:
            return (None, False, False)

        l, lp, lq = self.helper(root.left, p, q)
        r, rp, rq = self.helper(root.right, p, q)

        # print("at node: ", root.val)
        if root.val == p.val and (lq or rq):
            return (root, True, True)
        if root.val == q.val and (lp or rp):
            return (root, True, True)

        if lp and lq:
            return (l, True, True)
        
        if rp and rq:
            return (r, True, True)

        if (lp and rq) or (lq and rp):
            return (root, True, True)
        
        return (None, lp or rp or (root.val==p.val), lq or rq or (root.val==q.val))
        
            

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.helper(root, p, q)[0]
        