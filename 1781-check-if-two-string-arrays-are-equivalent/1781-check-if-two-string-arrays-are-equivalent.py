class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        wordone="".join(word1)
        wordtwo="".join(word2)
        if wordone==wordtwo:
            return True
        return False
        