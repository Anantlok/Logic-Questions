class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)

        for i in range(n - 1):  # i < n-1
            left = sum(nums[:i + 1])      # left includes index i
            right = sum(nums[i + 1:])     # right starts from i+1

            if (left - right) % 2 == 0:
                count += 1

        return count