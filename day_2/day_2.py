# Day 2 Advent of Code
from pathlib import Path
from typing import List

def parse_input(input_file: Path = Path(__file__).parent / "input.txt") -> List[List[int]]:
    input_path = input_file.absolute()

    all_vals = []

    with input_path.open(mode="r", encoding="utf-8") as file:
        for line in file:
            vals = line.strip("\n").split(" ")

            all_vals.append(vals)

    return all_vals

def analyse_reports(input_data: List[List[int]]) -> int:
    valid_reports = 0

    for i in range(len(input_data)):
        for j in range(len(input_data[i])):
            report_copy = input_data[i].copy()
            report_copy.pop(j)

            if is_valid(report_copy):
                valid_reports += 1
                break

    return valid_reports

def is_valid(report: List[int]) -> bool:
    diffs = [int(report[i+1]) - int(report[i]) for i in range(len(report)-1)]
    if (all(x < 0 and x in range(-3, 0) for x in diffs) or  
      all(x > 0 and x in range(1, 4) for x in diffs)):   
        return True
    else:
        return False 
                 
if __name__ == "__main__":
    input_data = parse_input()
    # print(input_data)
    print(f"valid reports: {analyse_reports(input_data)}")
