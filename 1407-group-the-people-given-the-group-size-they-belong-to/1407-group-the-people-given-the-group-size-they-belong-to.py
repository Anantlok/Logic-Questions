class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        mapp={}
        result=[]
        for i in range(len(groupSizes)):
            size=groupSizes[i]
            if size not in mapp:
                mapp[size]=[]
            mapp[size].append(i)
            if len(mapp[size])==size:
                result.append(mapp[size])
                mapp[size]=[]
        return result

        