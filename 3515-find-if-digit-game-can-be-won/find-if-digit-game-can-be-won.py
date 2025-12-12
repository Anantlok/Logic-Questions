class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        total = sum(nums)
        single = sum(x for x in nums if 1 <= x <= 9)
        double = sum(x for x in nums if 10 <= x <= 99)

        return (2 * single > total) or (2 * double > total)