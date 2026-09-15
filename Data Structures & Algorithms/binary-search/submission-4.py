class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r, m = 0, len(nums) - 1, len(nums) // 2

        while l <= r:
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
            m = l + ((r - l) // 2)

        return -1