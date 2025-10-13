class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def isanagram(a,b):
            return sorted(a)==sorted(b)
        stack=[]
        for word in words:
            if stack and isanagram(stack[-1],word):
                continue
            stack.append(word)
        return stack
        