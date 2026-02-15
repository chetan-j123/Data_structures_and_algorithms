class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        """
        Problem: 1480. Running Sum of 1D Array

        Given an array nums, return the running sum where
        runningSum[i] = sum(nums[0] ... nums[i])

        Time Complexity: O(n)
        Space Complexity: O(1) (in-place, no extra array)
        """

        total = nums[0]
        for i in range(1, len(nums)):
            total += nums[i]
            nums[i] = total

        return nums
