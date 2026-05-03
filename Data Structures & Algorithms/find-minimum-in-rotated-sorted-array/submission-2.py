class Solution:
    def findMin(self, nums: List[int]) -> int:
        L , R = 0 , len(nums) - 1
        print(L, R)

        if nums[L] <= nums[R]:
            min_val = nums[L]
        else:
            min_val = nums[R]

        #print(min_val)
        while L <= R:
            mid = L + (R - L) // 2

            if nums[mid] >= min_val:
                L = mid + 1
               # min_val = nums[mid]

            if nums[mid] <= min_val:
                R = mid - 1
                min_val = nums[mid]

        return min_val