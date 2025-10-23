class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s)>2:
            k=0
            sk=""
            for i in range(0,len(s)-1):
                k=(int(s[i])+int(s[i+1]))%10
                sk=sk+str(k)
            s=sk
        if(s[0]==s[1]):
            return True
        return False
            

        