class Solution:
    def trap(self, height: List[int]) -> int:
        rm=height[-1]
        lm=height[0]

        l,r=0,len(height)-1
        s=0
        while l<r:
            if lm<rm:
                l+=1
                lm=max(lm,height[l])
                s+=max(min(lm,rm)-height[l],0)
            else:
                r-=1
                rm=max(rm,height[r])
                s+=max(min(lm,rm)-height[r],0)

        return s

            
            
