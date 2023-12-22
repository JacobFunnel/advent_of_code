with open("input/02.txt", "r") as f:
    lines = f.read().split("\n")


def parse(line):
    policy, pwd = line.split(": ")
    char = policy[-1]
    low = policy[: policy.find("-")]
    high = policy[policy.find("-") + 1 : -2]
    return int(low), int(high), char, pwd


def validate(low, high, char, pwd):
    if (pwd[low - 1] == char) != (pwd[high - 1] == char):
        return True
    else:
        return False


def validate_lines(lines):
    valid = 0
    for line in lines:
        if validate(*parse(line)):
            valid += 1
    return valid


print(validate_lines(lines))
