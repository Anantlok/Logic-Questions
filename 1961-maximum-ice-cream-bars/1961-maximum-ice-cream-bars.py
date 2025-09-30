class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        scosts=sorted(costs)
        total=0
        count=0
        for i in scosts:
            total=total+i
            if total>coins:
                break
            count=count+1
        return count
        