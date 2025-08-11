class Solution(object):
    def strStr(self, haystack, needle):
        min_temp=None
        for i in range(0,len(haystack)):
            string1 = ""
            for j in range(i,i+len(needle)):
                if j<len(haystack):
                    string1 = string1 + haystack[j]
                else:
                    break
            if string1==needle:
                temp=i
                if min_temp is None or temp<min_temp:
                    min_temp=temp
        if min_temp != None:
            return (min_temp)
        if min_temp == None:
            return (-1)
        