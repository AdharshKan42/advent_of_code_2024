import re
from day_3 import parse_input

def parse_mult_enabled(text: str) -> int:
    # i copied giac's b/c I could not figure this regex out
    pattern = r"mul\((\d{1,3},\d{1,3})\)|(do\(\))|(don't\(\))"

    group = re.findall(pattern, text)

    muls =0
    do = True
    for val in group:
        if val[1] == "do()":
            do = True
        elif val[2] == "don't()":
            do = False
    
        if do and val[0] != "":
            mul = val[0].split(",")
            muls += int(mul[0]) * int(mul[1])

    return muls

if __name__ == "__main__":
    input_data = parse_input()
    print(f"total muls: {parse_mult_enabled(input_data)}")