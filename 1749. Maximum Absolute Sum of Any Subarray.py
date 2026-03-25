class Solution(object):
    def maxAbsoluteSum(self, nums):
        prev_max_sum=nums[0]
        prev_min_sum=nums[0]
        max_sum=nums[0]
        min_sum=nums[0]
        pointer=1
        while pointer <len(nums):    
            prev_max_sum = max(nums[pointer],nums[pointer]+prev_max_sum) 
            prev_min_sum=min(nums[pointer],nums[pointer]+prev_min_sum)
            max_sum=max(max_sum,prev_max_sum)
            min_sum=min(min_sum,prev_min_sum)
            pointer+=1 
        p=max(abs(max_sum),abs(min_sum))
        return p
