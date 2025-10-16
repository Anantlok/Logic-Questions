class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        k=[]
        for i in candies:
            if i+extraCandies>=max(candies):
                k.append(True)
            else:
                k.append(False)
        return k
        