class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        right=len(s)-1

        for left in range(0,len(s)):
            if left <right:
                s[right],s[left]=s[left],s[right]
                left+=1
                right-=1

        return s

        