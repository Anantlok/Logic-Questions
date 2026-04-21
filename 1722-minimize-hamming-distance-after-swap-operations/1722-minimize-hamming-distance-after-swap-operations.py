class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        parent = list(range(len(source)))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        # Step 1: Build components
        for a, b in allowedSwaps:
            union(a, b)

        groups = defaultdict(list)
        for i in range(len(source)):
            root = find(i)
            groups[root].append(i)

        # Step 2: Count mismatches
        res = 0
        for indices in groups.values():
            count = Counter()
            
            # Count source values
            for i in indices:
                count[source[i]] += 1
            
            # Match with target
            for i in indices:
                if count[target[i]] > 0:
                    count[target[i]] -= 1
                else:
                    res += 1

        return res
        