class Solution:
    def reverseBits(self, n: int) -> int:
        k=bin(n)[2:]
        thir=k.zfill(32)
        r="".join(thir)[::-1]
        return(int(r,2))
        