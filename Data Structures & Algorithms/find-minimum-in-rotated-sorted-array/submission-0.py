class Solution:
    def findMin(self, nums: List[int]) -> int:
        L , R = 0 , len(nums) - 1

        min_val = min(nums[L], nums[R])

        while L <= R:
            mid = L + (R - L) // 2

            if nums[mid] >= min_val:
                L = mid + 1
               # min_val = nums[mid]

            if nums[mid] <= min_val:
                R = mid - 1
                min_val = nums[mid]

        return min_val