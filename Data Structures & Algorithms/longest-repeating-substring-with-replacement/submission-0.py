class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = defaultdict(int)
        n = len(s)
        total = 0
        l = 0
        rep = 0
        ans = 0
        def check(ct, kt):
            for _, c in ct.items():
                if total - c <= kt:
                    return True
            return False
        for i in range(0,n):
            cnt[s[i]] += 1
            total += 1
            while not check(cnt, k):
                cnt[s[l]] -= 1
                total -= 1
                l += 1;
            ans = max(ans, i - l + 1)
        return ans
        