class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def counter(st):
            dic={}
            for i in st:
                dic[i]=dic.get(i,0)+1
            if dic.get('1',0)==0:
                return 0
            return dic['1']
        lis=[]
        for i in arr:
            lis.append([i,counter(bin(i))])
        lis.sort(key=lambda x:(x[1],x[0]))
        arr2=[x[0] for x in lis]
        return arr2
            
        