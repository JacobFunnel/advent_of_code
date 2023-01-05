with open("input/12.txt", "r") as f:
    lines = f.read().split("\n")
    commands = [(line[0], int(line[1:])) for line in lines]


def execute_commands(commands):
    body = Body()
    recipe = {"N": {"action": "move", "direction": (0, 1)},
              "E": {"action": "move", "direction": (1, 0)},
              "S": {"action": "move", "direction": (0, -1)},
              "W": {"action": "move", "direction": (-1, 0)},
              "L": {"action": "turn", "sign": -1},
              "R": {"action": "turn", "sign": 1},
              "F": {"action": "move"}
              }
    for instruction, amount in commands:
        body.act(**recipe[instruction], amount=amount)
    return abs(body.pos[0]) + abs(body.pos[1])


class Body:
    def __init__(self):
        self.pos = [0, 0]
        self.angle = 0
        self.directions = {0: (1, 0),
                           90: (0, -1),
                           180: (-1, 0),
                           270: (0, 1)}

    def get_direction(self, angle):
        return self.directions[angle % 360]

    def move(self, direction, amount):
        self.pos = [self.pos[0] + direction[0] * amount, self.pos[1] + direction[1] * amount]

    def turn(self, sign, amount):
        self.angle = (self.angle + sign * amount) % 360

    def act(self, action=None, direction=None, sign=None, amount=None):
        if action == "move":
            direction = direction or self.get_direction(self.angle)
            self.move(direction, amount)
        elif action == "turn":
            self.turn(sign, amount)


print(execute_commands(commands))
