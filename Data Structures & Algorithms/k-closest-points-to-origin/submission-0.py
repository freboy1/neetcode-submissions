import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for point in points:
            val = (point[0] ** 2 + point[1] ** 2) ** 0.5
            heapq.heappush(
                heap,
                (val,
                point)
            )

        answer = []
        for _ in range(k):
            distance, point = heapq.heappop(heap)
            answer.append(point)
        
        return answer