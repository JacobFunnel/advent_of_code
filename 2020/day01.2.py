with open("input/01.txt", "r") as f:
    nums = f.read().split("\n")

nums = [int(num) for num in nums]


def find_2020(nums):
    for a in nums:
        for b in nums:
            for c in nums:
                if a != b and b != c and a != c and a + b + c == 2020:
                    return a, b, c, a * b * c


print(find_2020(nums))
