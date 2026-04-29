class Solution:
    def trap(self, height: List[int]) -> int:
        L = 0
        R=len(height)-1
        max_l_list = []
        max_L  = 0
       # print(height[R])
        for i in range(R + 1):
          if i == 0:
            max_l_list.append(max_L)
          else:
            max_l_list.append(max(max_L, height[i-1]))
            max_L = max(max_L, height[i-1])   

       # print(len(height), len(max_l_list))
       # print(max_l_list)
        res = []
        max_r = 0
        while R > 0:

          min_right_left = min(max_l_list[R], max_r)
          if min_right_left - height[R] >= 0:
           res.append(min_right_left - height[R])
          else:
            res.append(0)
          R-=1
          max_r = max(max_r, height[R+1])
        return sum(res)

        
            
         
        