class Solution {
public:
    vector<int> countBits(int n) {
        std::vector<int> ans;
        int i = 0;
        int j;
        while (i <= n) {
            int count = 0;
            j = i;
            while (j > 0) {
                if (j%2) {
                    count++;
                }
                j = j/2;
            }
            ans.push_back(count);
            i++;
        }
        return ans;
    }
};
