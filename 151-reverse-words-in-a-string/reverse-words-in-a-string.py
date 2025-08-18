class Solution(object):
    def reverseWords(self, s):
        str=s.split()
        return " ".join(reversed(str))
        