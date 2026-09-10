# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        def lvl(root):
            ans = []
            queue = deque([])
            queue.append(root)

            while len(queue) != 0:
                level = []
                for i in range(len(queue)):
                    e = queue.popleft()
                    level.append(e.val)

                    if e.left is not None:
                        queue.append(e.left)
                    if e.right is not None:
                        queue.append(e.right)
                ans.append(level)

            return ans
        return lvl(root)

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
                
        