class Solution:
    def spent_hours(self, pile, speed):
        i = pile // speed
        if pile % speed != 0:
            i += 1
        return i


    def check(self, piles, speed, h):
        spent_hours = 0
        for pile in piles:
            spent_hours += self.spent_hours(pile, speed)
            if spent_hours > h:
                return False
        
        return True
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)

        while low <= high:
            mid = (low + high) // 2

            koko_result = self.check(piles, mid, h)
            
            if koko_result:
                high = mid - 1
            else:
                low = mid + 1
        return low







