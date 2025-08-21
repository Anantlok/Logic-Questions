class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        prefix=""
        min_length = min(len(word) for word in strs)
        for i in range(min_length):
            char=strs[0][i]
            for word in strs:
                if i>=len(word) or word[i]!=char:
                    return prefix
            prefix=prefix+char
        return prefix
        
        