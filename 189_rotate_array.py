from typing import List

class Solution:
    """
    LeetCode 189: Rotate Array
    Given an integer array nums, rotate the array to the right by k steps, 
    where k is non-negative.
    
    Approach: Three Reversals (In-place)
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        if n == 0:
            return
        
        # Handle cases where k > n
        k = k % n
        
        def reverse(first: int, last: int) -> None:
            while first < last:
                nums[first], nums[last] = nums[last], nums[first]
                first += 1
                last -= 1
        
        # Step 1: Reverse the whole array
        reverse(0, n - 1)
        # Step 2: Reverse the first k elements
        reverse(0, k - 1)
        # Step 3: Reverse the remaining elements
        reverse(k, n - 1)
