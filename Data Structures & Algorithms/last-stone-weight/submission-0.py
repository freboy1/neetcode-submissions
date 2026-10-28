import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-num for num in stones]
        heapq.heapify(max_heap)

        while (len(max_heap) > 1):
            max1 = -heapq.heappop(max_heap)
            max2 = -heapq.heappop(max_heap)

            if max1 > max2:
                heapq.heappush(max_heap, -(max1-max2))
            elif max1 < max2:
                heapq.heappush(max_heap, -(max2-max1))

        if len(max_heap) == 0:
            return 0
        return -max_heap[-1]