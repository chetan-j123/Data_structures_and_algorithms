class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        first=0
        second=0
        hashmap={}
        max_len=0
        while second<len(s):
            hashmap[s[second]]=hashmap.get(s[second],0)+1
            while hashmap[s[second]]>1:
                if hashmap[s[first]]==1:
                    del hashmap[s[first]]
                elif hashmap[s[first]]>1:
                    hashmap[s[first]]-=1
                first+=1
            max_len=max(max_len,second-first+1)
            second+=1
        return max_len
