class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=0
        right=0
        max_len=0
        max_1s=0
        zeroes=0
        while right<len(nums):
            if nums[right]==0:
                zeroes+=1
            else:
                max_1s+=1
            while (right-left+1)-max_1s>k:
                if nums[left]==0:
                      zeroes-=1
                elif nums[left]==1:
                      max_1s-=1
                left+=1
            max_len=max(right-left+1,max_len)
            right+=1
        return max_len
