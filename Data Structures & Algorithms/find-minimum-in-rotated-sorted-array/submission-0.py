class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_num = nums[0]
        l = 0
        r = len(nums) - 1
        m = (r - l) // 2

        while l <= r:
            if nums[l] < nums[m] and nums[l] > nums[r]:
                l = m + 1
            elif nums[l] < nums[m] and nums[l] < nums[r]:
                r = m - 1
            else:
                l += 1

            m = l + ((r - l) // 2)
            if nums[m] < min_num:
                min_num = nums[m]

        return min_num