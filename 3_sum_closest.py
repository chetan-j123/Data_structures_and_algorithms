from typing import List

class Solution:
    """
    LeetCode 16: 3Sum Closest
    Problem: Find three integers in nums such that the sum is closest to target.
    
    Approach: Sorting + Two Pointers. Track the 'mini' difference to find 
    the sum with the smallest absolute distance from the target.
    """
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        # Initialize with the sum of the first triplet minus target
        mini = (nums[0] + nums[1] + nums[n-1]) - target
        
        for i in range(n - 2):
            first = i + 1
            last = n - 1
            
            while first < last:
                current_sum = nums[i] + nums[first] + nums[last]
                current_diff = current_sum - target
                
                if current_diff == 0:
                    return target
                
                # Update mini if the current difference is smaller
                if abs(current_diff) < abs(mini):
                    mini = current_diff
                
                if current_diff < 0:
                    first += 1
                else:
                    last -= 1
                    
        return mini + target

if __name__ == "__main__":
    sol = Solution()
    print(f"3Sum Closest Result: {sol.threeSumClosest([-1, 2, 1, -4], 1)}")
