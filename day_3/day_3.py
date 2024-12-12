# Day 3 Advent of Code
from pathlib import Path

def parse_input(input_file: Path = Path(__file__).parent / "input.txt") -> str:
    input_path = input_file.absolute()

    txt = input_path.read_text().replace("\n", "")

    return txt

# Parses through input data and calculates total of valid mul values
def parse_mult(txt: str) -> int:
    mul_list = txt.split("mul")
    # Keep track of all multiplication sums
    muls = 0

    # If "mul" isn't found in this line, skip
    if len(mul_list) == 1:
        return 0

    for i in range(len(mul_list)):
        # Grab current value split between muls in original strings
        val = mul_list[i]

        if "(" in val and ")" in val:
            left_ptr = find_index_of_value("(", val)
            right_ptr = find_index_of_value(")", val)

            if left_ptr == 0 and right_ptr != -1 and right_ptr - left_ptr >= 4:
                muls += analyse_mul_vals(val[left_ptr+1: right_ptr])

    return muls

def find_index_of_value(val: str, s: str) -> int:
    try:
        return s.index(val)
    except ValueError:
        return -1

# Determines if a set of values within a mul() call are valid, returns the mul value if true
# Takes in parameters within a mul call, example 2,5 in mul(2,5)
def analyse_mul_vals(mul_val: str) -> int:
    params = mul_val.split(",")
    
    # If comma isn't found or there aren't 2 parameters found, return 0
    if len(params) < 2:
        return 0
    
    if params[0].isdigit() and params[1].isdigit():
        return int(params[0]) * int(params[1])
        
    return 0
    
if __name__ == "__main__":
    input_data = parse_input()
    print(f"total muls: {parse_mult(input_data)}")