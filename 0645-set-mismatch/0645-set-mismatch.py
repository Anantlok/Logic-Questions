class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        k=[]
        dic={}
        for i in range(0,len(nums)):
            dic[nums[i]]=dic.get(nums[i],0)+1
        for i in dic.items():
            print(i[0])
            if i[1]==2:
                k.append(i[0])
                    
        for i in range(1, len(nums)+1):
            if i not in dic.keys():
                k.append(i)
                break
        
        return k

                

        