class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::set<int> set1;
        for(int i = 0; i < nums.size(); i++){
            if(set1.contains(nums[i])){
                return true;
            }else{
                set1.insert(nums[i]);
            }
        }
        return false;
    }
};