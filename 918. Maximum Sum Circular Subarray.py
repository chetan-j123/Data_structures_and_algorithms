
class Solution(object):
    def maxSubarraySumCircular(self, nums):
        pointer=1
        minimum=nums[0]
        maximum=nums[0]
        prev_min_sum=nums[0]
        prev_max_sum=nums[0]
        total_sum=nums[0]
        while pointer <len(nums):
            prev_min_sum=min(nums[pointer],nums[pointer]+prev_min_sum)
            prev_max_sum=max(nums[pointer],nums[pointer]+prev_max_sum)
            total_sum+=nums[pointer]
            minimum=min(minimum,prev_min_sum)
            maximum=max(maximum,prev_max_sum)
            pointer+=1
        if total_sum==minimum:
            return maximum
        max_sum=max((total_sum-minimum),maximum)
        return max_sum
        
