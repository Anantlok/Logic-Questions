class Solution(object):
    def searchInsert(self, nums, target):
        li=[]
        for i in range(0,len(nums)):
            li.append(nums[i])
        li.append(target)
        li.sort()
        return li.index(target)
        