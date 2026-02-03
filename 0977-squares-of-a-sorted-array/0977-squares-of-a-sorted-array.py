class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        out=[0]*(len(nums))
        n=len(out)
        left=0
        right=n-1
        for i in range(n-1,-1,-1):
            if abs(nums[left])>abs(nums[right]):
                val=nums[left]
                left+=1
            else:
                val=nums[right]
                right-=1
            out[i]=val*val
        return out