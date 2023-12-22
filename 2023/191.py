import re

from parse import parse_lines
from collections import namedtuple

Part = namedtuple("Part", ["x", "m", "a", "s"])


def parse():
    workflows, parts = parse_lines(2)
    workflows = [wf[:-1].split("{") for wf in workflows.splitlines()]
    workflows = {name: rules.split(",") for name, rules in workflows}
    parts = [Part(*(int(n) for n in re.findall(r"\d+", line))) for line in parts.splitlines()]
    return workflows, parts


def eval_rule(part, rule):
    comparison_map = {"<": lambda a, b: a < b, ">": lambda a, b: a > b}
    if ":" in rule:
        attribute = rule[0]
        comparison_symbol = rule[1]
        value = int(re.findall(r"\d+", rule)[0])
        destination = rule[rule.find(":") + 1 :]
        if comparison_map[comparison_symbol](getattr(part, attribute), value):
            if destination in {"A", "R"}:
                return None, destination
            else:
                return destination, None
        else:
            return None, None
    elif rule in {"A", "R"}:
        return None, rule
    else:
        return rule, None


def test_part(part, workflows):
    status = None
    workflow = workflows["in"]
    while not status:
        for rule in workflow:
            next_workflow, status = eval_rule(part, rule)
            if next_workflow:
                workflow = workflows[next_workflow]
                break
            elif status:
                break
    return status


workflows, parts = parse()
total = 0
for part in parts:
    if test_part(part, workflows) == "A":
        total += part.x + part.m + part.a + part.s
print(total)
