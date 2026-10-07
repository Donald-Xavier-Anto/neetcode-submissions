class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int ans = 0, cnt = 1;
        for(int num: nums) {
            ans = ans ^ num ^ cnt;
            cnt++;
        }
        return ans;
    }
};
