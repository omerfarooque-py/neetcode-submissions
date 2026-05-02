class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R = len(matrix) - 1
        L = 0
       
        
        while L <= R:
            mid = L + (R - L) // 2

            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                #return matrix[mid] 
                key_list = matrix[mid]
                L = 0
                R = len(key_list)
                while L <= R:
                    mid = L + (R - L) // 2

                    if key_list[mid] == target:
                        return True

                    if key_list[mid] > target:
                        R = mid - 1

                    if key_list[mid] < target:
                        L = mid + 1
                return False
            
            if matrix[mid][0] > target:
                R = mid -1
            if matrix[mid][-1] < target:
                L = mid + 1

        return False
                



                
        