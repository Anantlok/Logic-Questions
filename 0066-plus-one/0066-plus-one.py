class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        output=[]
        k=""
        for i in digits:
            k+=str(i)
        kint=int(k)+1
        for i in str(kint):
            output.append(int(i))
        return output

        