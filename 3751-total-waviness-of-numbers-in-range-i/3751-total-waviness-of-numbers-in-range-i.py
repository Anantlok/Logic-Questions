class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def solve(x: int) -> int:
            if x < 0:
                return 0

            s = str(x)
            n = len(s)

            @lru_cache(None)
            def dp(pos, tight, started, p2, p1, length):
                if pos == n:
                    return (1, 0)  # one completed number, no extra waviness

                limit = int(s[pos]) if tight else 9

                total_cnt = 0
                total_wav = 0

                for d in range(limit + 1):
                    ntight = tight and (d == limit)

                    # still leading zeros
                    if not started and d == 0:
                        cnt, wav = dp(
                            pos + 1,
                            ntight,
                            False,
                            10, 10, 0
                        )
                        total_cnt += cnt
                        total_wav += wav
                        continue

                    if not started:
                        cnt, wav = dp(
                            pos + 1,
                            ntight,
                            True,
                            10, d, 1
                        )
                        total_cnt += cnt
                        total_wav += wav
                    else:
                        add = 0
                        if length >= 2:
                            if (p2 < p1 > d) or (p2 > p1 < d):
                                add = 1

                        cnt, wav = dp(
                            pos + 1,
                            ntight,
                            True,
                            p1,
                            d,
                            length + 1
                        )

                        total_cnt += cnt
                        total_wav += wav + add * cnt

                return (total_cnt, total_wav)

            return dp(0, True, False, 10, 10, 0)[1]

        return solve(num2) - solve(num1 - 1)