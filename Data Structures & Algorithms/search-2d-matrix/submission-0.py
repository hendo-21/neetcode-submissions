class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            l = 0
            r = len(row) - 1
            m = (len(row) - 1) // 2

            while l <= r:
                if row[m] > target:
                    r = m - 1
                elif row[m] < target:
                    l = m + 1
                else:
                    return True
                m = l + ((r - l) // 2)

        return False