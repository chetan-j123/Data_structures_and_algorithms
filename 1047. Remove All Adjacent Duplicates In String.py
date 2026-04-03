class Solution(object):
    def removeDuplicates(self, s):
        def isempty(t):
            if t:
                return False
            else:
                return True
     
        stack=[]
        for i in range(0,len(s),1):
            if not isempty(stack):
                if s[i]==stack[-1]:
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
        
        stack="".join(stack)
        return stack
        



        

        



        
