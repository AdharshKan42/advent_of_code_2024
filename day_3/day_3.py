# Day 3 Advent of Code
from pathlib import Path
from typing import List

def parse_input(input_file: Path = Path(__file__).parent / "input.txt") -> List[List[int]]:
    input_path = input_file.absolute()

    all_vals = []

    with input_path.open(mode="r", encoding="utf-8") as file:
        for line in file:
            all_vals.append(line.strip("\n"))

    return all_vals

if __name__ == "__main__":
    input_data = parse_input()
    print(input_data)
