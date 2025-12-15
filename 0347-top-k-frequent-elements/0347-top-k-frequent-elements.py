class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}        
        for i in nums:
            dic[i]=dic.get(i,0)+1
        print(dic)
        jk=sorted(dic.items(), key=lambda item: item[1],reverse=True)
        print(jk)
        lk=[]
        for i in range(0,k):
            lk.append(jk[i][0])
        return lk


        