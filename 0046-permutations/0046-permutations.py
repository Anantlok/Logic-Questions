class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def bc(path,used):
            if len(path)==len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i]=True
                bc(path,used)
                path.pop()
                used[i]=False
        bc([],[False]*len(nums))
        return res

        