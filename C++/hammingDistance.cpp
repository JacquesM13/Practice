class Solution {
public:
    int hammingDistance(int x, int y) {
        // converting int to binary
        std::vector<int> outx;
        std::vector<int> outy;
        int count = 0;
        while (x > 0 || y > 0) {
            outx.push_back(x%2);
            x /= 2;
            outy.push_back(y%2);
            y /= 2;
        }
        // std::reverse(outy.begin(), outy.end());
        // std::reverse(outx.begin(), outx.end());
        for (int i = 0; i < outy.size(); i++) {
            if (outy[i] != outx[i]) {
                count++;
            }
        }
        return count;
    }
};
