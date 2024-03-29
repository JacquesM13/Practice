class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int i=0,j=0;
        int n= nums.size();
        while(i<n && j<n){
        if(nums[i]==0 && nums[j]!=0){
          nums[i]=nums[j];
          nums[j] = 0;
        }else if(nums[i]!=0 && nums[j]==0){
            i++;
        }else j++;
    }
    }
};
