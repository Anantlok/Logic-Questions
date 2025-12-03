class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        result = []
        n = len(pattern)

        for i in range(n):
            stack.append(str(i+1))
            if pattern[i] == 'I':
                while stack:
                    result.append(stack.pop())

        # push last digit
        stack.append(str(n+1))
        while stack:
            result.append(stack.pop())

        return "".join(result)