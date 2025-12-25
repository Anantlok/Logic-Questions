class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
        p=" "
        for i in s:
            if i.isalnum():
                p=p+i
        if p=="".join(reversed(p)):
            return True
        else:
            return False
