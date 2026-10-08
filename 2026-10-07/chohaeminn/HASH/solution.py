def solution(nums):
    return min(len(nums)//2, len(set(nums)))
'''
from collections import Counter

return min(len(nums)//2 , len(Counter(nums)))

'''

'''
def solution(nums):
    max_select = len(nums) // 2

    ponketmon_dict = {}
    
    for num in nums:
        if num in ponketmon_dict:
            ponketmon_dict[num] += 1
        else:
            ponketmon_dict[num] = 1

    unique_count = len(ponketmon_dict)

    return min(max_select, unique_count)
'''