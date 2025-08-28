from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join([ch * freq for ch, freq in sorted(Counter(s).items(), key=lambda x: -x[1])])