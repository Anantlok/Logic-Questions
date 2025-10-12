class Solution:
    def isBalanced(self, num: str) -> bool:
        eve=0
        odd=0
        for i in range(0,len(num)):
            if i%2==0:
                eve=eve+int(num[i])
            if i%2==1:
                odd=odd+int(num[i])
        if eve==odd:
            return True
        else:
            return False

        