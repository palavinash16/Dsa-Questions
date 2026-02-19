class Solution(object):
    def reverse(self, x):
        
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0
        INT_MAX = 2**31 - 1

        while x != 0:
            pop = x % 10
            x //= 10
            # check overflow before pushing pop
            if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and pop > INT_MAX % 10):
                return 0
            rev = rev * 10 + pop

        return sign * rev


        
        
    
        