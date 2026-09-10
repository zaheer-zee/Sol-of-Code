# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        ans = True

        def balance(root):
            nonlocal ans
            if root is None:
                return 0
            left = balance(root.left)
            right = balance(root.right)

            if abs(left - right) > 1:
                ans = False
            
            return 1 + max(left,right)
        balance(root)
        return ans
        