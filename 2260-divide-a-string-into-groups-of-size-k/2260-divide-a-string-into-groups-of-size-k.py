class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        se=len(s)%k
        if(se>0):
            s=s+fill*(k-se)
        kk=""
        db=[]
        for i in range(0,len(s)):
            kk=kk+s[i]
            if len(kk)>k-1:
                db.append(kk)
                kk=""
        return db
        