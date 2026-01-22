class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def is_sorted(arr):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    return False
            return True
        
        operations = 0
        
        while not is_sorted(nums):
            min_sum = float('inf')
            idx = 0
            
            # find leftmost adjacent pair with minimum sum
            for i in range(len(nums) - 1):
                if nums[i] + nums[i + 1] < min_sum:
                    min_sum = nums[i] + nums[i + 1]
                    idx = i
            
            # merge the pair
            nums = nums[:idx] + [nums[idx] + nums[idx + 1]] + nums[idx + 2:]
            operations += 1
        
        return operations
        