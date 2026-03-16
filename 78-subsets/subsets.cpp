class Solution {
public:
    vector<vector<int>> result;

    void backtrack(int start, vector<int>& nums, vector<int>& curr) {
        result.push_back(curr);   // store current subset
        
        for(int i = start; i < nums.size(); i++) {
            curr.push_back(nums[i]);       // include
            backtrack(i + 1, nums, curr); // explore
            curr.pop_back();              // backtrack
        }
    }

    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> curr;
        backtrack(0, nums, curr);
        return result;
    }
};