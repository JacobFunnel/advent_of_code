import re
from collections import Counter

with open("input/19.txt", "r") as f:
    numbers = [tuple(map(int, re.findall(r'\d+', line))) for line in f.read().splitlines()]

blueprints = {n1: {"ore_bot": Counter({"ore": n2}),
                   "clay_bot": Counter({"ore": n3}),
                   "obs_bot": Counter({"ore": n4, "clay": n5}),
                   "geo_bot": Counter({"ore": n6, "obs": n7})}
              for n1, n2, n3, n4, n5, n6, n7 in numbers}


def can_afford(cost, bank):
    return all(bank[mineral] >= amount for mineral, amount in cost.items())


def harvests(bot):
    return bot[:bot.find("_")]


def production(blueprint):
    bank = Counter({"ore": 0, "clay": 0, "obs": 0, "geo": 0})
    bots_in_duty = Counter({"ore_bot": 1, "clay_bot": 0, "obs_bot": 0, "geo_bot": 0})
    bots_in_training = Counter({"ore_bot": 0, "clay_bot": 0, "obs_bot": 0, "geo_bot": 0})
    priority = ["geo_bot", "obs_bot", "clay_bot", "ore_bot"]
    for minute in range(24):
        # buy bots
        for bot in priority:
            while can_afford(blueprint[bot], bank):
                bank -= blueprint[bot]
                bots_in_training[bot] += 1
        # harvest minerals
        bank += Counter({harvests(bot): amount for bot, amount in bots_in_duty.items()})
        # update bots
        bots_in_duty += bots_in_training
        bots_in_training.clear()
    return bank["geo"]


for idx, blueprint in blueprints.items():
    print(f"{idx}, geo: {production(blueprint)}")
