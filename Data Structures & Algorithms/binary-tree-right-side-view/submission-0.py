# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        q = deque()
        ans = []
        q.append(root)
        while len(q) != 0:
            sz = len(q)
            for i in range(0,sz):
                f = q.popleft()
                if i == sz-1:
                    ans.append(f.val)
                if f.left != None:
                    q.append(f.left)
                if f.right != None:
                    q.append(f.right)
        return ans
        