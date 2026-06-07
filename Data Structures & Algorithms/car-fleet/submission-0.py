class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        s = sorted(zip(position, speed), key = lambda x: x[0])
        t = [0]*len(speed)
        for (p, sp) in s:
            t.append((target-p)/sp)
        # car_fleet = 0
        st = []
        for i in t:
            while len(st)>0 and st[-1]<=i:
                st.pop()
            st.append(i)
        return len(st)