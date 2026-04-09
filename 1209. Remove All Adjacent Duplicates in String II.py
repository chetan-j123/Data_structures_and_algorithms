class Solution(object):
    def removeDuplicates(self, s, k):
        stack=[]
        for i in range(0,len(s),1):
            if stack and stack[-1][0]==s[i]:
                stack[-1][1]+=1
            else:
                stack.append([s[i],1])
            if k==stack[-1][1]:
                stack.pop()
        # stack me agr pop krke niakte jaye to stack me elemnts humne froward traverse se dale the wo stack se revrse order me nikallneg
        str="".join(stack[i][0]*stack[i][1] for i in range(len(stack)))# here stack ki frowar traversing ho rhi h to hume origginal order me hi string milegi 
        return str
                    
        
