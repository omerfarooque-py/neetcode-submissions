class Solution:
    def search(self, nums: List[int], target: int) -> int:
    
        L = 0
        R =  len(nums) - 1
        mid = L + (R - L) // 2
  
        while L != R+1:

            if nums[L] == target:
                return L
            if nums[R] == target:
                return R
            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                R = mid - 1
                mid = L + (R - L) // 2
            elif nums[mid] < target:
                L = mid + 1
                mid = L + (R - L) // 2

        return -1
        