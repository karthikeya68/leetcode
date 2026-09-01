class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max=0
        a=0
        b=len(height)-1
        for i in range (len(height)):
            x=min(height[a],height[b])*(b-a)
            if(x> max):
                max=x
            if(height[a]<height[b]):
                a+=1
            else:
                b-=1
        return max


        