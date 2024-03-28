#include <typeinfo>
class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        vector<char> merge;
        std::string mergeS;
        if (word1.length() > word2.length()) {
            for (int i = 0; i < word1.length(); ++i) {
                merge.push_back(word1[i]);
                if (i < word2.length()) {
                    merge.push_back(word2[i]);
                } 
            }
        } else {
            for (int i = 0; i < word2.length(); ++i) {
                if (i < word1.length()) {
                    merge.push_back(word1[i]);
                }
                merge.push_back(word2[i]);
            }
        }
        for (char k : merge) {
            mergeS += k;
        }
    return mergeS;
    }
};
