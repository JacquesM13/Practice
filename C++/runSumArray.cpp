class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> ans;
        int j = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (i == 0) {
                ans.push_back(nums[i]);
                continue;
            }
            ans.push_back(nums[i] + ans[j]);
            j++;
        }
        
        // for (int k : ans) {
        //     std::cout << k;
        // }
        return ans;
    }
};
