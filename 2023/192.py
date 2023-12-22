import re
import operator

from parse import parse_lines
from collections import namedtuple

Part = namedtuple("Part", ["x", "m", "a", "s"])
Rule = namedtuple("Rule", ["repr", "attribute", "comparison_function", "value", "destination"])
comparison_map = {"<": operator.lt, ">": operator.gt}


class Node:
    def __init__(self, workflow, rules, parent, parent_trigger):
        self.workflow = workflow
        self.rules = rules
        self.parent = parent
        self.parent_trigger = parent_trigger
        self.children = set()
        self.end = None
        self.end_trigger = None

    def __repr__(self):
        if self.parent_trigger is None:
            start = "I"
        else:
            start = f"{self.parent_trigger} then i"
        if self.end_trigger is None:
            end = ""
        else:
            end = f" {self.end_trigger}"
        return f"{start}f {self.rules[0].repr} ({self.workflow}) {end}"


def parse_rule(rule):
    attribute = None
    comparison_function = None
    value = None
    if ":" in rule:
        attribute = rule[0]
        comparison_function = comparison_map[rule[1]]
        value = int(re.findall(r"\d+", rule)[0])
        destination = rule[rule.find(":") + 1 :]
        repr = rule[: rule.find(":")]
    else:
        repr = ""
        destination = rule
    return Rule(repr, attribute, comparison_function, value, destination)


def parse():
    workflows, parts = parse_lines(2)
    workflows = [wf[:-1].split("{") for wf in workflows.splitlines()]
    workflows = {name: [parse_rule(rule) for rule in rules.split(",")] for name, rules in workflows}
    parts = [Part(*(int(n) for n in re.findall(r"\d+", line))) for line in parts.splitlines()]
    return workflows, parts


def define_children(node):
    global nodes
    rule = node.rules[0]
    if rule.comparison_function:
        # true path
        if rule.destination in {"A", "R"}:
            node.end = rule.destination
            node.end_trigger = True
        else:
            nodes.append(Node(rule.destination, workflows[rule.destination], node, True))
            node.children.add(nodes[-1])
        # false path
        nodes.append(Node(node.workflow, node.rules[1:], node, False))
        node.children.add(nodes[-1])
    else:
        if rule.destination in {"A", "R"}:
            node.end = rule.destination
            node.end_trigger = False
        else:
            nodes.append(Node(rule.destination, workflows[rule.destination], node, False))
            node.children.add(nodes[-1])
    for child in node.children:
        define_children(child)


workflows, parts = parse()
nodes = [Node("in", workflows["in"], None, None)]
define_children(nodes[0])

paths = []
for node in nodes:
    if node.end == "A":
        paths.append([node])
        while paths[-1][-1].parent is not None:
            next_node = paths[-1][-1]
            paths[-1].append(next_node.parent)

# paths = [[node for node in path if len(node.rules) > 1 or node.end] for path in paths]
print([list(reversed(path)) for path in paths])
