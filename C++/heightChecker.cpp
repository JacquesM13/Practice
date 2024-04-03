class Solution {
public:
    int heightChecker(vector<int>& heights) {
        // sort the vector to get expected
        std::vector<int> heights2 (heights.begin(), heights.end());
        std::sort(heights2.begin(), heights2.end());
        int count = 0;
        for (int i = 0; i < heights.size(); i++) {
            if (heights[i] != heights2[i]) {
                count++;
            }
        }
        return count;
    }
};
