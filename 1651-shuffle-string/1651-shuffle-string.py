class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s1=list(s)
        k=list(s)
        count=0
        for i in indices:
            k[i]=s1[count]
            count=count+1
        return "".join(k)
