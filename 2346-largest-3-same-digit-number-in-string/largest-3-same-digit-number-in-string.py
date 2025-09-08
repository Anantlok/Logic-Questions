class Solution:
    def largestGoodInteger(self, num: str) -> str:
        k=[]
        for i in range(0,len(num)-2):
            if num[i]==num[i+1] and num[i]==num[i+2]:
                k.append(int(num[i]*3))
        if len(k)==0:
            return ""
        m=max(k)
        if m==0:
            return (str(m)*3)
        return str(m)
                
        