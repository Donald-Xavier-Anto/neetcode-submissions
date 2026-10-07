class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        int ans = 0;
        for(int i=0;i<31;i++) {
            ans = ans | ((n>>i) & 1);
            ans = ans<<1;
        }
        ans = ans | ((n>>31) & 1);
        return ans;
    }
};
