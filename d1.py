import re

def part_one():

    with open(file="in.txt") as f:
        final_sum = 0
        lines = f.read().splitlines()
        for line in lines:
            digits = [char for char in line if char.isdigit()]
            final_sum += int(digits[0] + digits[-1])

        return(final_sum)

def part_two():

    final_sum = 0
    digit_words = "one two three four five six seven eight nine".split()
    #pattern = "(?=(" + "|".join(digit_words) + "|\\d))"
    pattern = "(?=(one|two|three|four|five|six|seven|eight|nine|\d))"


    def helper_func(x):
        if x in digit_words:
            return str(digit_words.index(x) + 1)
        return x

    for line in open("in.txt").read().splitlines():
        digits = [*map(helper_func, re.findall(pattern, line))]
        final_sum += int(digits[0] + digits[-1])

    return(final_sum)
    
if __name__ == "__main__":
    print(part_one())
    print(part_two())
