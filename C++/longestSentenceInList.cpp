class Solution {
public:
    int mostWordsFound(vector<string>& sentences) {
        int count;
        vector<int> sizes;
        for (int i = 0; i < sentences.size(); i++) {
            string sentence = sentences[i];
            count = 1;
            char b = ' ';
            for (char k : sentence) {
                if (k == b) {
                    count ++;
                }
            }
            sizes.push_back(count);
        }
    return *max_element(sizes.begin(), sizes.end());
    }
};
