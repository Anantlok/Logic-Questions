class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxk=[]
        for i in range(0,len(sentences)):
            k=sentences[i]
            k1=k.split(" ")
            
            maxk.append(len(k1))
            print(maxk)
        return max(maxk)