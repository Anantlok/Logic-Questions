class Solution:
    def finalString(self, s: str) -> str:
        k=""
        for i in s:
            if i=="i":
                re="".join(reversed(k))
                k=re
            else:
                k=k+i
        return k
        