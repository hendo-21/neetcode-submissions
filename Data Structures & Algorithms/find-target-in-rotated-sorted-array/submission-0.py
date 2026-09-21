class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + ((r - l) // 2)
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1

        if nums[l] <= target <= nums[-1]:
            r = len(nums) - 1
        else:
            r = l - 1
            l = 0

        while l <= r:
            m = l + ((r - l) // 2)
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                return m

        return -1