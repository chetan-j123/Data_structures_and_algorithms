class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
     nums.sort()
     mini=(nums[0]+nums[1]+nums[len(nums)-1])-target 
     for i in range(0,len(nums)-2,1):
            last=len(nums)-1
            first=i+1
            while last>first:  
                current_ele=(nums[first]+nums[last]+nums[i])-target 
                if current_ele==0:
                    return (current_ele+target)
                elif current_ele<0: 
                    if abs(mini)>abs(current_ele):
                          mini=current_ele
                    first+=1
                elif current_ele>0 :
                    if abs(mini)>abs(current_ele):
                          mini=current_ele
                    last=last-1
     return(mini+target)
