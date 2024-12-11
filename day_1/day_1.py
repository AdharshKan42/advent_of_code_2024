# Day 1 Advent of Code
from pathlib import Path
from collections import Counter
from typing import List


def parse_input(input_file: Path = None) -> list[list[int]]:
    l1 = []
    l2 = []

    if input_file is None:
        input_file = Path(__file__).parent / "input.txt"
    input_path = input_file.absolute()

    print(input_path)
    with input_path.open(mode="r", encoding="utf-8") as file:
        for line in file:
            vals = line.strip("\n").split("   ")
            # print(vals)
            # print(int(vals[1]))
            # print("************")
            l1.append(int(vals[0]))
            l2.append(int(vals[1]))

    assert len(l1) == len(l2)
    return [sorted(l1), sorted(l2)]

def find_total_distance(input_data: list[list[int]]) -> int:
    total = 0
    for i in range(len(input_data[0])):
        total += abs(input_data[0][i] - input_data[1][i])
    return total    

def get_sim_score(l1: List[int], l2: List[int]) -> int:
    score = 0
    l2_counts = Counter(l2)
    for i in range(len(l1)):
        if l1[i] in l2_counts:
            score += (l1[i] * l2_counts[l1[i]])

    return score

if __name__ == "__main__":
    input_data = parse_input()
    # print(input_data)
    # print(find_total_distance(input_data))
    print(f"sim score: {get_sim_score(input_data[0], input_data[1])}")

