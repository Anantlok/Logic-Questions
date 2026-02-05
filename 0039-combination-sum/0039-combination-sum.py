class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def bc(start,path,remain):
            if remain==0:
                res.append(path[:])
                return
            if remain<0:
                return
            for i in range(start,len(candidates)):
                path.append(candidates[i])
                bc(i,path,remain-candidates[i])
                path.pop()
        bc(0,[],target)
        return res