class Solution:
    def trap(self, height: List[int]) -> int:
        slow = 0
        water = 0
        begin_max = height[0]
        loc_max = None

        for fast in range(1, len(height)):
            if height[fast] >= begin_max and fast != slow:
                while slow < fast:
                    water += (begin_max - height[slow])
                    slow += 1
                begin_max = height[fast]
                loc_max = None
            
            elif (loc_max is None or height[fast] >= height[loc_max])  and fast != slow:
                print("fast ", height[fast])
                loc_max = fast

        length = len(height) - 1
        height_max = 0
        remain_water = 0
        while slow <= length:
            if height[length] > height_max:
                # remain_water = 0
                height_max = height[length]
            else:
                # temp_water = 
                remain_water += (height_max - height[length])
            length -= 1


        print("slow ", slow)
        print("loc_max ", loc_max)
        print("remain", remain_water)
        return water + remain_water