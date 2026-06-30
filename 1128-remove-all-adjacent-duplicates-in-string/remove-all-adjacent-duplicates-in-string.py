class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        for ch in s:
            if len(stack)==0:
                stack.append(ch)

            else:
                if stack[-1]==ch:
                    stack.pop()
                else:
                    stack.append(ch)
        return "".join(stack)
        