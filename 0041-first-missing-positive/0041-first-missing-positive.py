class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        while i<n:
            if 0<nums[i]<=n:
                curr=nums[i]-1
                if nums[curr]!=nums[i]:
                    nums[i],nums[curr]=nums[curr],nums[i]
                    continue
            i+=1
        for i in range(n):
            if nums[i]!=i+1:
                print(nums)
                return i+1
        return n+1