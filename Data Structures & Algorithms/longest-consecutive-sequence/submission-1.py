class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        temp = 1
        nums = list(set(nums))
        if len(nums) == 1:
            return 1
        nums.sort()
        # print(nums)
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i+1]:
               temp += 1
            else:
                temp = 1

            if temp > longest:
                longest = temp

        return longest