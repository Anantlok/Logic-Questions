class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        output=[]
        for i in words:
            k=i.split(separator)
            for j in k:
                if j:
                    output.append(j)
        return output
        