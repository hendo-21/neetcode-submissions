class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        l = 1
        r = max(piles)
        m = max(r // 2, 1)
        
        while l <= r:
            ct = 0
            for pile in piles:
                ct += -(pile // -m)
            if ct > h:
                l = m + 1
            elif ct <= h:
                r = m - 1
                k = m
            m = max(l + ((r - l) // 2), 1)

        return k