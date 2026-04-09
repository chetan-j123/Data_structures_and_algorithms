class Solution(object):
    def firstUniqChar(self, s):
        hashmap={}
        for i in range(0,len(s),1):
              hashmap[s[i]]=hashmap.get(s[i],0)+1
        for  i in range(0,len(s),1):
           if hashmap[s[i]]==1:
            return i
        return -1
            
