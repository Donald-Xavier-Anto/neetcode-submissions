class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt = defaultdict(int)
        window = defaultdict(int)
        for i in s1:
            cnt[i] += 1
        for i in range(0,len(s2)):
            window[s2[i]] += 1
            # print(window)
            if i >= len(s1)-1:
                if cnt == window:
                    return True
                window[s2[i-len(s1)+1]] -= 1
                if window[s2[i-len(s1)+1]] == 0:
                    window.pop(s2[i-len(s1)+1])
        return False
        