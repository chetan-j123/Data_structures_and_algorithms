class Solution:
    def isPalindrome(self, s: str) -> bool:
        first=0
        last=len(s)-1
        val=True
        while last>first:
         if not s[first].isalnum() :
            first+=1
         elif  not s[last].isalnum():
            last-=1
         elif s[last].lower()!= s[first].lower():
            val=False
            break
         elif s[last].lower()==s[first].lower():
            first+=1
            last-=1
        return val
