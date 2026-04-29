class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left_list = [0] * n
        max_left = 0
        for i in range(n-1): 
            max_left_list[i] = max_left
            max_left = max(max_left, height[i])
        max_right = 0
        water = 0
        for i in range(n-1, -1, -1):
            water += max(0, min(max_left_list[i], max_right) - height[i])
            max_right = max(max_right, height[i])
        return water

        
            
         
        