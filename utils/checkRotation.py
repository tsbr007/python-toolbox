class CheckRotation:

    @staticmethod
    def are_rotation(s1: str, s2: str) -> bool:
        self_concat = s1 + s1
        return s2 in self_concat

if __name__ == "__main__":
    print(CheckRotation.are_rotation("abcd", "cdab"))  # True
    print(CheckRotation.are_rotation("abcd", "cbad"))  # False
