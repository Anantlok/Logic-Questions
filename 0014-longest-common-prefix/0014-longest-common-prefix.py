class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        st="" #123
        for i in strs[0]:
            flag=False
            for j in range(0,len(strs)):
                if i in strs[j]:
                    flag=True
                else:
                    flag=False
                    break
            if flag==True:
                st+=i
        return st
        