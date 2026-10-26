class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        answer = []

        for sub_str in strs:
            sorted_str = "".join(sorted(sub_str))
            if sorted_str in dic:
                temp_index = dic[sorted_str]
                answer[temp_index].append(sub_str)
            else:
                answer.append([sub_str])
                dic[sorted_str] = len(answer) - 1
                
        return answer