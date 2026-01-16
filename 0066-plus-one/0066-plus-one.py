class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        k="".join(str(i) for i in digits)
        k1=str(int(k)+1)
        return [int(i) for i in k1]