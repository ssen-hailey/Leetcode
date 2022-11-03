class Solution(object):
    def runningSum(self, nums):
        #runningSum=[]
        for i in range(1,len(nums)):
            nums[i]=nums[i-1]+nums[i]
            
        return nums
        """
        :type nums: List[int]
        :rtype: List[int]
        """
   