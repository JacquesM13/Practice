class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int> out;
        for (int k : nums) {
            int gt = 0;
            for (int j : nums) {
                if (k > j) {
                    gt++;
                }
            }
            out.push_back(gt);
        }
        return out;
    }
};
