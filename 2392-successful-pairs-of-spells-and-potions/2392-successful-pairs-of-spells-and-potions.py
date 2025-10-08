class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        output=[]
        potion=sorted(potions)
        m=len(potions)
        for i in spells:
            minn=(success+i-1)//i
            left,right=0,m-1
            while left<=right:
                mid=(left+right)//2
                if potion[mid]<minn:
                    left=mid+1
                else:
                    right=mid-1
            output.append(m-left)
        return output

        