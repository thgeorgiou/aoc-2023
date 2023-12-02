digits_p1 = {str(i): i for i in range(10)}
digits_p2 = digits_p1 | {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def find_calibration_value(input: str, digit_map: dict[str, int]) -> int:
    value = 0

    for line in input.splitlines():
        line = line.strip()
        if not line:
            continue

        for i in range(len(line)):
            for key in digit_map.keys():
                if line[i:].startswith(key):
                    start = digit_map[key]
                    break

        for i in range(len(line), -1, -1):
            for key in digit_map.keys():
                if line[:i].endswith(key):
                    end = digit_map[key]
                    break

        print(line, start, end)

        value += 10 * end
        value += start

    return value


test_str_1 = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

print(f"Test, part 1: {find_calibration_value(test_str_1, digits_p1)}")

test_str_2 = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

print(f"Test, part 2: {find_calibration_value(test_str_2, digits_p2)}")

with open("input", "r") as f:
    input_str = f.read()
    print(f"Part 1: {find_calibration_value(input_str, digits_p1)}")
    print(f"Part 2: {find_calibration_value(input_str, digits_p2)}")
