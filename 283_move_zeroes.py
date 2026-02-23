from typing import List

class Solution:
    """
    LeetCode 283: Move Zeroes
    Given an integer array nums, move all 0's to the end of it while 
    maintaining the relative order of the non-zero elements.
    
    Approach: Two Pointers (Read/Write)
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    def moveZeroes(self, nums: List[int]) -> None:
        first = 0  # Write pointer
        
        for i in range(len(nums)):  # i is the Read pointer
            if nums[i] != 0:
                # Swap elements or overwrite and clear
                if i != first:
                    nums[first] = nums[i]
                    nums[i] = 0
                first += 1
