class Solution:
    def addDigits(self, num: int) -> int:
        if len(str(num))==1:
            return num
        ab=str(num)
        sum=0
        for i in ab:
            sum=sum+int(i)
            num=sum
        return self.addDigits(num)
        