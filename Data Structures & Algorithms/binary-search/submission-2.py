class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums) - 1
        L = 0
        R = n
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
        