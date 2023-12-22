import os
import sys


def parse_lines(n=1):
    with open(f"input/{os.path.basename(sys.argv[0])[:2]}.txt", "r") as f:
        return f.read().split("\n" * n)
