class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # strategy: identify a sequence starting element then build a streak
        # checking to see if each streak element is in the hashmap
        if not nums:
            return 0
        
        hash_set = set(nums)
        streak = 1
        longest, count = 1, 1

        for num in nums:
            if num - 1 not in hash_set:
                while num + count in hash_set:
                    count += 1
                longest = max(longest, count)
                count = 1
        return longest