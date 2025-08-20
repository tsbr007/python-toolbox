def get_two_sum(nums, target):
    pair = {}
    for i, num in enumerate(nums):
        if num in pair:
            return [pair[num], i]
        else:
            pair[target - num] = i
    return []


if __name__ == "__main__":
    print(get_two_sum([2, 7, 11, 15], 9))