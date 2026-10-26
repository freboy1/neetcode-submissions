class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}


        for i in range(len(nums)):
            dic[nums[i]] = i
        
        for i in range(len(nums)):
            value = target - nums[i]
            if value in dic and i != dic[value]:
                return [i, dic[value]]
        
        return [0, 0]