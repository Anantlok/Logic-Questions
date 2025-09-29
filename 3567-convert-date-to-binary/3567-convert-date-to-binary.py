class Solution:
    def convertDateToBinary(self, date: str) -> str:
        ks=date.split("-")
        p=""
        for i in ks:
            p=p+bin(int(i))[2:]+"-"
        return p[:len(p)-1]
        