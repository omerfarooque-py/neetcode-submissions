class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights)-1
        max_area = 0
        while L < R:
           if (min(heights[L],heights[R]) * (R - L)) > max_area:
              max_area = (min(heights[L],heights[R]) * (R - L))
           if heights[L] >= heights[R]:
             R-=1
           if heights[L] < heights[R]:
            L+=1
        return max_area

             
            
                