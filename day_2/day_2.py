import re


def prod(*args: int) -> int:
    res = args[0]
    for x in args[1:]:
        res *= x
    return res


def parse_instance(instance_str: str):
    tokens = [x.strip() for x in instance_str.split(",")]
    instance = {}
    for x in tokens:
        count, color = x.split(" ")
        instance[color] = int(count)
    return instance


def parse(input_str: str):
    games = {}
    for line in input_str.splitlines():
        if not line.startswith("Game"):
            continue

        id = re.findall("Game ([0-9]+)", line)[0]
        showings = line.split(":")[1].split(";")
        game = [parse_instance(x) for x in showings]

        games[int(id)] = game

    return games


def get_minimum_contents(g: list[dict[str, int]]):
    return {
        "red": max([i.get("red", 0) for i in g]),
        "green": max([i.get("green", 0) for i in g]),
        "blue": max([i.get("blue", 0) for i in g]),
    }


def test_game(game: dict[str, int], targets: dict[str, int]):
    for k, v in targets.items():
        if v < game[k]:
            return False
    return True


def solve(input_str, target):
    part_1 = 0
    part_2 = 0
    for id, g in parse(input_str).items():
        contents = get_minimum_contents(g)
        if test_game(contents, target):
            part_1 += id
        part_2 += prod(*contents.values())
    return part_1, part_2


test_target = {"red": 12, "green": 13, "blue": 14}
test_input = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

test_1 = solve(test_input, test_target)
print(f"Test answer {test_1}")

with open("input", "r") as f:
    inp = f.read()
    part_1, part_2 = solve(inp, test_target)
    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")
