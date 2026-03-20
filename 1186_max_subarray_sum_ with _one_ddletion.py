from typing import List

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        no_del = arr[0]
        one_del = 0
        result = arr[0]

        for i in range(1, len(arr)):
            x = arr[i]

            one_del = max(no_del, one_del + x)
            no_del = max(x, no_del + x)

            result = max(result, no_del, one_del)

        return result
