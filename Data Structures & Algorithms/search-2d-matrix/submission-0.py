class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_r = 0 
        r_r = len(matrix)-1

        while(l_r <= r_r):
            mid = (l_r+r_r)//2
            val = matrix[mid][0]

            if target == val:
                return True
            elif target > val:
                l_r = mid + 1
            else:
                r_r = mid - 1
        # here r_r is the matrix we shd search
        l = 0 
        r = len(matrix[r_r])-1

        while(l<=r):
            mid = (l+r)//2
            val = matrix[r_r][mid]

            if target == val :
                return True
            elif target > val :
                l = mid + 1
            else:
                r = mid - 1
        return False