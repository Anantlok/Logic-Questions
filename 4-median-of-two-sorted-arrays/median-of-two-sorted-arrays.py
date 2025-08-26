class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a=nums1+nums2
        c=sorted(a)
        if len(c)%2==1:
            return float(c[int(len(c)/2)])
        if len(c)%2==0:
            return (c[int(len(c)/2)]+c[int(len(c)/2)-1])/2

        