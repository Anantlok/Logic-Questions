class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d=[]
        dic={}
        for i in nums:
            dic[i]=dic.get(i,0)+1
        for key, values in dic.items():
            if float(values)>(len(nums)/3):
                d.append(key)
        return d        