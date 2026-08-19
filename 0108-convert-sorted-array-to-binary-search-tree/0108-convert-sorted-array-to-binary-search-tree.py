# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def binary(nums,l,h):
            if l > h:
                return None
            mid = (l + h) // 2
            root = TreeNode(nums[mid])
            root.right = binary(nums,mid + 1,h)
            root.left = binary(nums,l,mid - 1)

            return root 
        return binary(nums,0,len(nums) - 1)
        