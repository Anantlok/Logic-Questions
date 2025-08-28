class Solution:
    def totalMoney(self, n: int) -> int:
        weeks=(n//7)+1
        sums=0
        days=0
        start=0
        for i in range(weeks):
            start+=1
            for j in range(start,start+7):
                if days==n:
                    break
                days=days+1
                sums=sums+j
        return sums
        