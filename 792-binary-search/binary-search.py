class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left=0
        right=len(nums)-1
        ans=-1

        while(left<=right):
            mid=left + (right-left)//2

            if target==nums[mid]:
                ans=mid
                right=mid-1
            elif target < nums[mid]:
                right=mid-1
            else:
                left=mid+1
        return ans
        