# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        ans = []
        final = []

        def check(root,lvl):
            if root is None:
                return 
            if lvl == len(ans):
                ans.append([])

            ans[lvl].append(root.val)

            check(root.left,lvl+1)
            check(root.right,lvl+1)

        check(root,0)

        for i in ans:
            final.append(i[0])
        
        return final[-1]

        