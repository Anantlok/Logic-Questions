class Solution(object):
    def searchRange(self, nums, target):
        n=[]
        for i in range(0,len(nums)):
            if(nums[i]==target):
                n.append(i)
        if not n:
            return [-1,-1]
        
        else:
            return [n[0],n[-1]]

        
