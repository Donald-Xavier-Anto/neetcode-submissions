import bisect
class TimeMap:
    def __init__(self):
        self.mp = defaultdict(list)
        self.st = set()

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append((value, timestamp))
        self.st.add(key)

    def get(self, k: str, timestamp: int) -> str:
        if k not in self.st:
            return ""
        ind = bisect.bisect_right(self.mp[k], timestamp, key = lambda x: x[1]) - 1
        if ind == -1:
            return ""
        return self.mp[k][ind][0]

