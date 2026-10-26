class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        start = 0
        end = len(heights) - 1
        while start <= end:
            temp_height = min(heights[start], heights[end])
            temp_area = (end - start)  * temp_height

            if temp_area > max_area:
                max_area = temp_area

            if heights[start] > heights[end]:
                end -= 1
            else:
                start += 1


        return max_area

        return max_area