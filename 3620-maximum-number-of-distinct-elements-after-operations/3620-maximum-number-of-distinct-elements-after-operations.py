class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        intervals = [(num - k, num + k) for num in nums]
        intervals.sort(key=lambda x: x[1])

        next_free = -10**18  # very small initial value
        count = 0

        for l, r in intervals:
            if next_free < l:
                next_free = l
            if next_free <= r:
                count += 1
                next_free += 1  # move to next available integer

        return count