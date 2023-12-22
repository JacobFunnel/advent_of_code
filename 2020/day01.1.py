with open("input/01.txt", "r") as f:
    nums = f.read().split("\n")

nums = [int(num) for num in nums]


def find_2020(nums):
    for a in nums:
        for b in nums:
            if a != b and a + b == 2020:
                return a, b, a * b


print(find_2020(nums))
