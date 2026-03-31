class Solution(object):
    def intervalIntersection(self, firstList, secondList):
         first=0
         second=0
         new_list=[]
         while first<len(firstList) and second<len(secondList):
            start=max(firstList[first][0],secondList[second][0])
            end=min(firstList[first][1],secondList[second][1])
            # if overlaps
            if end>=start:
                new_list.append([start,end])
            if firstList[first][1]<secondList[second][1]:
                # mtlb first list ka intervall chhota h 
                first+=1
            else:
                #second ka chhota h 
                second+=1
         return new_list
