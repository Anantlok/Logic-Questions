class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set=set(wordDict)
        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True
        for i in range(0,n+1):
            for w in word_set:
                if i>=len(w) and dp[i-len(w)] and s[i-len(w):i]==w:
                    dp[i]=True
                    break
        return dp[n]
        