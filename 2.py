
fruit_limits = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

def check_fruits(set: str) -> bool:
    # part 1
    fruits = set.split(',')
    for fruit in fruits:
        num, val = fruit.strip().split(' ')
        if int(num) > fruit_limits[val]:
            return False
    return True

def check_min_fruits(set: str, min_fruits: dict) -> dict:
    # part 2
    fruits = set.split(',')
    for fruit in fruits:
        num, val = fruit.strip().split(' ')
        if int(num) > min_fruits[val]:
            min_fruits[val] = int(num)
    return min_fruits

def process_game(game: str) -> int:
    game, sets = game.split(':')
    sets = sets.split(';')
    min_fruits={"red": 0, "green": 0,"blue": 0}
    for set_ in sets:
        min_fruits = check_min_fruits(set_, min_fruits)
    result = 1
    for v in min_fruits.values():
        result *= v
    return result

with open("2_input.txt", "r") as file:
    games = file.read().splitlines()

games_ok = [process_game(game) for game in games]

print(sum(games_ok))