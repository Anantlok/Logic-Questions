class Solution:
    def reverseVowels(self, s: str) -> str:
        
        sk = list(s)
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        vowel_list = [ch for ch in s if ch in vowels]
        vowel_list.reverse()
        idx = 0
        for i in range(len(sk)):
            if sk[i] in vowels:
                sk[i] = vowel_list[idx]
                idx += 1
        return "".join(sk)        