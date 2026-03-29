class Solution(object):
    def pivotIndex(self, nums):
        prefix=0#i=0
        total=0
        for k in range(len(nums)):
            total+=nums[k]
        for j in range (0,len(nums),1):
             if j-1>=0:    
               prefix+=nums[j-1] 
             if prefix==total-nums[j]-prefix:
                return j
        return -1
       

