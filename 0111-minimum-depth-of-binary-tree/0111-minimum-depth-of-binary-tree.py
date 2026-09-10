# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        def check(root):
            if root is None:
                return 0

            if root.right is None:
                return 1 + check(root.left)

            if root.left is None:
                return 1 + check(root.right)
            
            return 1 + min(check(root.left),check(root.right))
        return check(root)
                
        