
def get_first_digit(in_str: str) -> str:
    for i in range(len(in_str)):
        for digit in digits:
            if in_str[i:i+len(digit)] == digit:
                return digit if len(digit) == 1 else str(digits.index(digit))

def get_last_digit(in_str: str) -> str:
    in_str_reverted = in_str[::-1]
    for i in range(len(in_str_reverted)):
        for digit in digits_reverted:
            if in_str_reverted[i:i+len(digit)] == digit:
                return digit if len(digit) == 1 else str(digits_reverted.index(digit))

digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
          "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
digits_reverted = [d[::-1] for d in digits]

with open("1_input.txt", "r") as file:
    lines = file.read().splitlines()

digits = [int(get_first_digit(line) + get_last_digit(line)) for line in lines]

print(sum(digits))