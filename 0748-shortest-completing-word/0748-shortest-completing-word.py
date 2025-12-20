from collections import Counter
from typing import List
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        required = Counter(ch.lower() for ch in licensePlate if ch.isalpha())

        result = None

        for word in words:
            word_count = Counter(word)

            # Check if word contains all required letters
            if all(word_count[c] >= required[c] for c in required):
                if result is None or len(word) < len(result):
                    result = word

        return result