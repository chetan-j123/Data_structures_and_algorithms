class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:    
            first=0
            second=0
            product=1
            count=0
            while second<len(nums):
             product=product*nums[second]
             while product>=k and not  (first>second) :
                    product=product//nums[first]
                    first+=1 
             count=count+second-first+1      
             second+=1
            return count
