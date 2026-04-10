# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def build(nums):
            if not nums:
                return None
            
            # Step 1: Find max element and its index
            max_val = max(nums)
            index = nums.index(max_val)
            
            # Step 2: Create root
            root = TreeNode(max_val)
            
            # Step 3: Build left and right recursively
            root.left = build(nums[:index])
            root.right = build(nums[index+1:])
            
            return root
        
        return build(nums)
        