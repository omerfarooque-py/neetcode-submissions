class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
           # print(stack)
            start = i
            while stack and stack[-1][1] > h:
                index, height =  stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append((start, h)) 
        #print(stack)
        for i, h in stack:
           # print(max_area, h, "*", len(heights), "-", i )
            max_area = max(max_area, h * (len(heights) - i ))
        return max_area