class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        sk=""
        for i in words:
            sk=sk+i[0]
        return sk==s
        