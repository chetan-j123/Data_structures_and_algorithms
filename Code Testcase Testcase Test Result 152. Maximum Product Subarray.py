class Solution(object):
    def maxProduct(self, nums):
        prev=nums[0]
        mini=nums[0]
        max_product=nums[0]
        pointer=1
        while pointer <len(nums):
            prev_temp=max(nums[pointer],nums[pointer]*prev,nums[pointer]*mini)
            mini_temp=min(nums[pointer],nums[pointer]*prev,nums[pointer]*mini)
            max_product=max(prev_temp,max_product)
            prev=prev_temp
            mini=mini_temp
            pointer+=1
        return max_product            
        
