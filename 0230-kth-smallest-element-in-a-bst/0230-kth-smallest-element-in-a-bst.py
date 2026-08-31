# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        def answer(root,k):
            if root is None:
                return None
            if root is not None:
                answer(root.left,k)
                ans.append(root.val)
                answer(root.right,k)
            return root
        answer(root,k)
        return ans[k-1]

        