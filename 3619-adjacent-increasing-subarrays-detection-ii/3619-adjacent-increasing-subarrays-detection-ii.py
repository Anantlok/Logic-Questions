class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: 
            return 0

        
        left = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                left[i] = left[i - 1] + 1

        # Right increasing lengths
        right = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                right[i] = right[i + 1] + 1

        ans = 0
        
        for mid in range(1, n):
            k = min(left[mid - 1], right[mid])
            ans = max(ans, k)

        return ans