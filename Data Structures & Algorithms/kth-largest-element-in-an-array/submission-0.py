import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-num for num in nums]
        i = 1

        heapq.heapify(max_heap)

        while i < k:
            heapq.heappop(max_heap)
            i += 1
        
        return -heapq.heappop(max_heap)