# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        def level(root,depth):
            if root is None:
                return
            if len(ans) == depth:
                ans.append([])
            ans[depth].append(root.val)

            level(root.left, depth+1)
            level(root.right,depth + 1)
        level(root,0)
        return ans
        # ans = []
        # def level(root):
        #     if root is None:
        #         return
        #     ans5 = []
        #     if root.right is not None and root.left is not None:
        #         ans5.append(root.left.val)
        #         ans5.append(root.right.val)
        #     elif root.left is not None:
        #         ans5.append(root.left.val)
        #     elif root.right is not None:
        #         ans5.append(root.right.val)
        #     elif root is not None and root.right is not None and root.left is not None:
        #         ans5.append(root.val)
        #     level(root.right)
        #     ans.append(ans5)
        #     level(root.left)
        # level(root)
        # return ans
                
        