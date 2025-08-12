class Solution(object):
    def isPalindrome(self, x):
        y=str(x)
        z="".join(reversed(y))
        if y==z:
            return True
        else:
            return False 
        