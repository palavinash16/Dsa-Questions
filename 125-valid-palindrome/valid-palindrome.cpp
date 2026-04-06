class Solution {
public:
bool checkPalindrome(string &s, int left, int right) {
    
    
    if(left >= right)
        return true;

    // Skip non-alphanumeric characters
    if(!isalnum(s[left]))
        return checkPalindrome(s, left + 1, right);

    if(!isalnum(s[right]))
        return checkPalindrome(s, left, right - 1);

    // Compare characters
    if(tolower(s[left]) != tolower(s[right]))
        return false;

    // Recursive call
    return checkPalindrome(s, left + 1, right - 1);
}

    bool isPalindrome(string s) {
        return checkPalindrome(s, 0, s.length() - 1);

        
    }
};