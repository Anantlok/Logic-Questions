class Solution:
    def conversion(self, arr:list[int]):
        k=0
        for i in range(0,len(arr)):
            if arr[i]==1:
                k=k+(-2)**(len(arr)-1-i)
        return k
    def conversion2(self,k):
        if k == 0:
            return [0]
        negabinary = []
        while k != 0:
            k, remainder = divmod(k, -2)
            if remainder < 0:
                remainder += 2
                k += 1
            negabinary.append(remainder)
        return negabinary[::-1]
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c=self.conversion(arr1)+self.conversion(arr2)
        return self.conversion2(c)

        
        