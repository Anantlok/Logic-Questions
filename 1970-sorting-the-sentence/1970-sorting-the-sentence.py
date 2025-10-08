class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ")
        output = [""] * len(words)

        for i in words:
            output[int(i[-1]) - 1] = i[:-1]

        return " ".join(output)
        