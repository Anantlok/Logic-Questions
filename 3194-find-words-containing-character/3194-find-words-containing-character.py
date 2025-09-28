class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        o=[]
        for i in range(0,len(words)):
            if x in words[i]:
                o.append(i)
        return o

        