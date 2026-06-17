class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = defaultdict(int)
        for i in s:
            cnt[i] += 1
        print(cnt)
        for i in range(0, len(s)):
            if cnt[s[i]] == 1:
                return i
        return -1