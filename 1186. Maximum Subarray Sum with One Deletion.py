class Solution(object):
    def maximumSum(self, arr):            
        prev_subarray_sum_without_deletion=arr[0]
        prev_subarray_sum_with_deletion=arr[0]
        maximum_sum=arr[0]
        pointer=1
        while pointer<len(arr):
            prev_subarray_sum_with_deletion=max(prev_subarray_sum_with_deletion+arr[pointer],prev_subarray_sum_without_deletion) 
            prev_subarray_sum_without_deletion=max(prev_subarray_sum_without_deletion+arr[pointer],arr[pointer])
            maximum_sum=max(maximum_sum,prev_subarray_sum_with_deletion,prev_subarray_sum_without_deletion)
            pointer+=1
        return maximum_sum
            
                
