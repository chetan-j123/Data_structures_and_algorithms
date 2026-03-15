class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left =0
        right=0
        hashmmap={}
        max_len=0
        while right <len(fruits):
            hashmmap[fruits[right]]=hashmmap.get(fruits[right],0)+1
            while  len(hashmmap)>2 and left<len(fruits):
                hashmmap[fruits[left]]-=1
                if hashmmap[fruits[left]]==0:
                 del hashmmap[fruits[left]]
                left +=1
            max_len=max(max_len,right-left+1)
            right+=1
        return max_len
