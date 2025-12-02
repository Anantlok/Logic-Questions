class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        def backtrack(start, comb, total):
                if len(comb) == k and total == n:
                    result.append(list(comb))
                    return
                if len(comb) > k or total > n:
                    return

                for i in range(start, 10):
                    comb.append(i)
                    backtrack(i + 1, comb, total + i)
                    comb.pop()
        backtrack(1, [], 0)
        return result
                