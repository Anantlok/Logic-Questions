class Solution:
    def findComplement(self, num: int) -> int:
        b=(bin(num)[2:])
        d=""
        for i in b:
            if i=="0":
                d=d+"1"
            if i=="1":
                d=d+"0"
        return(int(d,2))
        