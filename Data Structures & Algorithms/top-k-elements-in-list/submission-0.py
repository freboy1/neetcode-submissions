class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for num in nums:

            if num not in dic:
                dic[num] = 0
            
            dic[num] += 1
        
        answer = []

        # print("original:", dic)

        sorted_items = sorted(
            dic.items(),
            key=lambda item: item[1],
            reverse=True
        )

        # print("sorted items:", sorted_items)

        sorted_dict = dict(sorted_items)

        # print("sorted dict:", sorted_dict)



        for key in sorted_dict.keys():
            answer.append(key)
            if len(answer) == k:
                return answer