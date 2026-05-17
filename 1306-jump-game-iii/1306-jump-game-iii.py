class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visted= set()
        def dfs(i):
            if i<0 or i>=len(arr) or i in visted:
                return False
            if arr[i]==0:
                return True
            visted.add(i)
            return dfs(i+arr[i]) or dfs(i-arr[i])
        return dfs(start)