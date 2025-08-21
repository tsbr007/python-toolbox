def get_sq_root(num: int) -> float:
    start = 0
    end = num
    mid = num / 2

    while mid != start:
        if mid * mid == num:
            return mid
        elif mid * mid > num:
            end = mid
        else:
            start = mid
        mid = (end + start) / 2

    return num


if __name__ == "__main__":
    print(get_sq_root(256))