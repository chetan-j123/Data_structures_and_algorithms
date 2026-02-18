from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        """
        LeetCode 1431: Kids With the Greatest Number of Candies

        Approach:
        - Find the maximum number of candies among all kids
        - For each kid, check if candies[i] + extraCandies >= max_candies

        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        result = [0] * len(candies)
        max_candies = max(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candies:
                result[i] = True
            else:
                result[i] = False

        return result
