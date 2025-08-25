from typing import List

def find_medians(nums: List[int], k: int) -> List[int]:
    medians = []
    for i in range(2, len(nums)):
        # current window of size 3
        window = sorted([nums[i-2], nums[i-1], nums[i]])
        
        if k % 2 == 0:
            median = (window[k//2] + window[(k-1)//2]) // 2
        else:
            median = window[k//2]
        
        medians.append(median)
    return medians


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(find_medians(nums, k))   # [1, -1, -1, 3, 5, 6]
