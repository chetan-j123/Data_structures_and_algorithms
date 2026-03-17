class Solution(object):
    def hasCycle(self, head):
       slow=head
       fast=head
       while fast!=None and   slow.next !=None and fast.next!=None and fast.next.next!=None :
         slow=slow.next
         fast=fast.next.next
         if slow==fast:
            return True
       return False

