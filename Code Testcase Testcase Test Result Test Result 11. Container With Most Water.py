class Solution:
    def maxArea(self, height: List[int]) -> int:
        first=0
        last=len(height)-1
        max_water=0
        if height[first]<=height[last]:
                        min=height[first]
        else:
                        min=height[last]
        while first<last:
                if height[first]<=height[last]:
                        min=height[first]
                else:
                        min=height[last]
                if (min*(last-first))>=max_water:
                        max_water=min*(last-first)
                if height[first]>=height[last]:
                    const=height[last]
                    last-=1
                    while  const>height[last] and last!=first:
                       last-=1     
                elif height[last]>height[first] :
                     const=height[first]
                     first+=1
                     while const>height[first] and last!=first:
                       first+=1
        return max_water
