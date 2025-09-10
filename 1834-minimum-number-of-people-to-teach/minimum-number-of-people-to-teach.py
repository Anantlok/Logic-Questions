class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        from collections import defaultdict
        user_langs = {i + 1: set(langs) for i, langs in enumerate(languages)}
        need_to_fix = []
        for u, v in friendships:
            if user_langs[u].intersection(user_langs[v]) == set():
             need_to_fix.append((u, v))

        if not need_to_fix:
            return 0  # All friends can already communicate
    
    
        min_to_teach = float('inf')
    
        for lang in range(1, n + 1):
            to_teach = set()
            for u, v in need_to_fix:
                if lang not in user_langs[u]:
                    to_teach.add(u)
                if lang not in user_langs[v]:
                    to_teach.add(v)
            min_to_teach = min(min_to_teach, len(to_teach))

        return min_to_teach
        