class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) - 1
        container = 0
        while L < R:
          if heights[L] >= heights[R]:
            print(L, R)
            area = heights[R] * (R - L)
            container = max(area, container)
            R-=1
          if heights[L] <= heights[R]:
            print(L, R)
            area = heights[L] * (R - L)
            container = max(area, container)
            L+=1
        return container


