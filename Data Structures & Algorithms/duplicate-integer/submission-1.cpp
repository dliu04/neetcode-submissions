class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        vector<int> history;

        for (int i = 0; i < nums.size(); i++) {
            for (int j = 0; j < history.size(); j++) {
                if (history[j] == nums[i])
                    return true;
            }
            history.push_back(nums[i]);
        }

        return false;
    }
};
