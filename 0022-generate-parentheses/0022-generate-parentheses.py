class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        def backtrack(curr,oc,cc):
            if len(curr)==2*n:
                result.append(curr)
                return
            if oc<n:
                backtrack(curr+"(",oc+1,cc)
            if cc<oc:
                backtrack(curr+")",oc,cc+1)
        backtrack("",0,0)
        return result

        