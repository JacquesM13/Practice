class Solution {
public:
    int hammingWeight(int n) {
        // array to store binary number
        int binaryNum[32], count = 0;
        // counter for binary array
        int i = 0;
        while (n > 0) {
            binaryNum[i] = n % 2;
            if (binaryNum[i] == 1) {
                count++;
            }
            n = n / 2;
            i++;
        }
        return count;
    }
};
