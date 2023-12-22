from parse import parse_lines


class Game:
    def __init__(self, s):
        number, sets = s.split(": ")
        self.number = int(number.split()[-1])
        self.sets = [Set(substring) for substring in sets.split("; ")]

    def __repr__(self):
        return f"#{self.number}: {self.sets}"

    def most_seen(self):
        r_max = max(_set.r for _set in self.sets)
        g_max = max(_set.g for _set in self.sets)
        b_max = max(_set.b for _set in self.sets)
        return Set(f"{r_max} red, {g_max} green, {b_max} blue")


class Set:
    def __init__(self, s):
        self.r, self.g, self.b = 0, 0, 0
        self.parse_set(s)

    def __repr__(self):
        r, g, b = self.r, self.g, self.b
        return f"({r=}, {g=}, {b=})"

    def __le__(self, other):
        return self.r <= other.r and self.g <= other.g and self.b <= other.b

    def parse_set(self, s):
        colors = {"red": 0, "green": 0, "blue": 0}
        for substring in s.split(", "):
            amount, color = substring.split()
            colors[color] = int(amount)
        self.r, self.g, self.b = colors.values()


games = [Game(raw_game) for raw_game in parse_lines()]
total = 0
for game in games:
    minimum = game.most_seen()
    total += minimum.r * minimum.g * minimum.b

print(total)
