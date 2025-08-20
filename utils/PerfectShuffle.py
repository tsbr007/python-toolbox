def is_perfect_shuffle(s1: str, s2: str, s3: str) -> bool:
    if len(s1) != len(s2) or len(s3) != 2 * len(s1):
        return False
    a_then_b = ''.join(a + b for a, b in zip(s1, s2))
    b_then_a = ''.join(b + a for a, b in zip(s1, s2))
    return s3 == a_then_b or s3 == b_then_a


if __name__ == "__main__":
    s1, s2 = "ABCD", "1234"
    print(is_perfect_shuffle(s1, s2, "A1B2C3D4"))  # True
    print(is_perfect_shuffle(s1, s2, "1A2B3C4D"))  # True
    print(is_perfect_shuffle(s1, s2, "1AB2C3D4"))  # False