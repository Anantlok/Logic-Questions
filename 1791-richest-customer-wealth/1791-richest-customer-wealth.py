class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        output=[]
        for i in accounts:
            output.append(sum(i))
        return max(output)
        