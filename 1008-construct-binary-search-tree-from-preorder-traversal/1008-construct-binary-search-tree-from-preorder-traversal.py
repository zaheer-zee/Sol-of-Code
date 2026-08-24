# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        i = 0
        def create(minVal,maxVal):
            nonlocal i
            if i == len(preorder):
                return None
            if preorder[i] < minVal or preorder[i] > maxVal:
                return None
            root = TreeNode(preorder[i])
            i+=1
            root.left = create(minVal,root.val)
            root.right = create(root.val,maxVal)

            return root
        return create(-float('inf'),float('inf'))
            
        # d = preorder[0]
        # root = TreeNode(d)
        # def create(root,lis,i):
        #     if i >= len(lis):
        #         return 
        #     if lis[i] > root.val:
        #         root.right = create(TreeNode(lis[i]),lis,i+1)
                
        #     elif lis[i] < root.val:
        #         root.left = create(TreeNode(lis[i]),lis,i+1)
                
        #     create(root.left,lis,i)
        #     create(root.right,lis,i)
        # tip = create(root,preorder,1)
        # return tip

        # for i in range(1,len(preorder)):
        #     if preorder[i] < root.val:
        #         root.left = TreeNode(preorder[i])
        #     if preorder[i] > root.val:
        #         root.right = TreeNode(preorder[i])
        # return root

        