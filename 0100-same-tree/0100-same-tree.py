# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        arr1=[]
        arr2=[]
        def preorder(node,arr):
            if not node:
                return
            arr.append(node.val)
            arr.append(preorder(node.left,arr))
            arr.append(preorder(node.right,arr))
        preorder(p,arr1)
        preorder(q,arr2)
        if arr1==arr2:
            return True
        return False