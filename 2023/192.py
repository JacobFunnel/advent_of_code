import re
import operator
from itertools import pairwise, islice, product
from math import prod

from parse import parse_lines
from collections import namedtuple

Part = namedtuple("Part", ["x", "m", "a", "s"])
Rule = namedtuple(
    "Rule", ["representation", "attribute", "comparison_function", "value", "destination"]
)


def tuple_comparison(fn):
    def comp(tup, n):
        return fn(tup[0], n) and fn(tup[1], n)

    return comp


comparison_map = {"<": operator.lt, ">": operator.gt}


class Node:
    def __init__(self, workflow, rules, parent, parent_trigger):
        self.workflow = workflow
        self.rules = rules
        self.rule = rules[0]
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
        return f"{start}f {self.rules[0].repr} ({self.workflow}){end}"


def batched(iterable, n):
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError("n must be at least one")
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        yield batch


def parse_rule(rule):
    attribute = None
    comparison_function = None
    value = None
    if ":" in rule:
        attribute = rule[0]
        comparison_function = comparison_map[rule[1]]
        value = int(re.findall(r"\d+", rule)[0])
        destination = rule[rule.find(":") + 1 :]
        representation = rule[: rule.find(":")]
    else:
        representation = ""
        destination = rule
    return Rule(representation, attribute, comparison_function, value, destination)


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
            # only an end node for the True path, false path can still continue
        else:
            nodes.append(Node(rule.destination, workflows[rule.destination], node, True))
            node.children.add(nodes[-1])
        # false path
        if len(node.rules[1:]) == 1:
            if node.rules[-1].destination in {"A", "R"}:
                node.end = node.rules[-1].destination
                node.end_trigger = False
            else:
                nodes.append(
                    Node(
                        node.rules[-1].destination,
                        workflows[node.rules[-1].destination],
                        node,
                        False,
                    )
                )
                node.children.add(nodes[-1])
        else:
            nodes.append(Node(node.workflow, node.rules[1:], node, False))
            node.children.add(nodes[-1])

    for child in node.children:
        define_children(child)


def construct_ranges(paths):
    comparisons = {}
    for path in paths:
        for node in path:
            if node.rule.comparison_function:
                comparisons.setdefault(node.rule.attribute, set()).add(
                    (node.rule.value, node.rule.repr[1])
                )
    ranges = {}
    for attribute, comparison_list in comparisons.items():
        endpoints = []
        for value, mouth in sorted(comparison_list):
            offset = -1 if mouth == "<" else 1
            endpoints += sorted([value, value + offset])
        ranges[attribute] = list(batched([1] + endpoints + [4000], 2))
    return ranges


def limit_attribut_values(paths):
    valid_parts = []
    for path in paths:
        valid_parts.append(construct_ranges(paths))
        part = valid_parts[-1]
        for node, next_node in pairwise(path):
            comp_fn = tuple_comparison(node.rule.comparison_function)
            part[node.rule.attribute] = [
                tup
                for tup in part[node.rule.attribute]
                if comp_fn(tup, node.rule.value) == next_node.parent_trigger
            ]
        last_node = path[-1]
        comp_fn = tuple_comparison(last_node.rule.comparison_function)
        part[last_node.rule.attribute] = [
            tup
            for tup in part[last_node.rule.attribute]
            if comp_fn(tup, last_node.rule.value) == last_node.end_trigger
        ]

    return valid_parts


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

paths = [list(reversed(path)) for path in paths]
parts = limit_attribut_values(paths)
combinations = [list(product(*part.values())) for part in parts]
unique_combos = set()
for part in parts:
    unique_combos |= set(product(*part.values()))
total = 0
for combo in unique_combos:
    total += prod(high - low + 1 for low, high in combo)
print(total)
