with open("input/12.txt", "r") as f:
    lines = f.read().split("\n")
    commands = [(line[0], int(line[1:])) for line in lines]


def execute_commands(commands):
    body = Body()
    recipe = {
        "N": {"action": "move_wp", "direction": (0, 1)},
        "E": {"action": "move_wp", "direction": (1, 0)},
        "S": {"action": "move_wp", "direction": (0, -1)},
        "W": {"action": "move_wp", "direction": (-1, 0)},
        "L": {"action": "rotate", "sign": -1},
        "R": {"action": "rotate", "sign": 1},
        "F": {"action": "move_body"},
    }
    for instruction, amount in commands:
        body.act(**recipe[instruction], amount=amount)
    return abs(body.pos[0]) + abs(body.pos[1])


class Body:
    def __init__(self):
        self.pos = [0, 0]
        self.wp_offset = [10, 1]

    def move_wp(self, direction, amount):
        self.wp_offset = [
            self.wp_offset[0] + direction[0] * amount,
            self.wp_offset[1] + direction[1] * amount,
        ]

    def move_body(self, amount):
        self.pos = [
            self.pos[0] + amount * self.wp_offset[0],
            self.pos[1] + amount * self.wp_offset[1],
        ]

    def rotate_90(self, sign):
        self.wp_offset = [sign * self.wp_offset[1], sign * -1 * self.wp_offset[0]]

    def act(self, action=None, direction=None, sign=None, amount=None):
        if action == "move_wp":
            self.move_wp(direction, amount)
        elif action == "move_body":
            self.move_body(amount)
        elif action == "rotate":
            for rotations in range(int(amount / 90)):
                self.rotate_90(sign)


print(execute_commands(commands))
