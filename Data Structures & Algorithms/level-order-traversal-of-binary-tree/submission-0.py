# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        q = deque()
        ans = []
        q.append(root)
        while len(q) != 0:
            sz = len(q)
            l = []
            for i in range(0,sz):
                f = q.popleft()
                l.append(f.val)
                if f.left != None:
                    q.append(f.left)
                if f.right != None:
                    q.append(f.right)
            ans.append(l)
        return ans

        