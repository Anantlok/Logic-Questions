class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        k=nums[0]
        def bubblesort(arr):
            for i in range(0,len(arr)):
                for j in range(len(arr)-i-1):
                    if arr[j+1]<arr[j]:
                        arr[j],arr[j+1]=arr[j+1],arr[j]
            return arr
        rest=bubblesort(nums[1:])
        print(k,rest[0],rest[1])
        return k+rest[0]+rest[1]
        