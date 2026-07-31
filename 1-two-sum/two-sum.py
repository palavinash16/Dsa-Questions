class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
     
        '''i=0
        j=len(nums)-1
        while i<=j:
            sum=nums[i]+nums[j]
            if sum==target:
                return [i, j]
            elif sum>target:
                j-=1
            elif sum<target:
                i+=1
        
            else:
                return [-1, -1]'''
        hm={}
        for i, num in enumerate(nums):
            req=target -num

            if req in hm:
                return [hm[req], i]
            hm[num] =i
        return []

            
            