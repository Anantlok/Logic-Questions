class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index = {ch: i for i, ch in enumerate(s)}
        stack = []
        used = set()
        
        for i, ch in enumerate(s):
            if ch in used:
                continue
            
            while stack and ch < stack[-1] and last_index[stack[-1]] > i:
                used.remove(stack.pop())
            
            stack.append(ch)
            used.add(ch)
        
        return "".join(stack)
        