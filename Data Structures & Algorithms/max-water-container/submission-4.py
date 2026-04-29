class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) - 1
        container = 0
        while L < R:
            H = min(heights[L], heights[R])
            area = H * (R - L)
            container = max(area, container)
            if heights[L] < heights[R]:
              L+=1
            else:
              R-=1
        return container


