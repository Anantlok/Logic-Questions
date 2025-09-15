class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        d=text.split()
        count=0
        for i in d:
            flag=True
            for j in brokenLetters:
                if j in i:
                    flag=False
            if flag==False:
                count=count+1
        return (len(d)-count)

        