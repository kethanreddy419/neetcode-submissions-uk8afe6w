class Solution:
    def trap(self, height: List[int]) -> int:
        lm=[]
        ml=height[0]
        for i in range(len(height)):
            if i==0:
                lm.append(0)
            else:
                if ml<height[i-1]:
                    ml=height[i-1]
                lm.append(ml)
        print(lm)
        rm=[]
        mr=height[-1]
        for i in range(len(height)-1,-1,-1):
            if i==len(height)-1:
                rm.append(0)
            else:
                if mr<height[i+1]:
                    mr=height[i+1]
                rm.append(mr)
            
        rm=rm[::-1]
        print(rm)
        s=0
        for i in range(len(height)-1):
            s+=max(min(rm[i],lm[i])-height[i],0)
        return s

#Max of left and max of right but both maxes need to be taller than the current height
#So the question is how can I can calculate the max left and right heights from each position 
#So that we can have a O(n) solution.