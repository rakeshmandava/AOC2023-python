def part_one(lines):
    total = 0
    for id, game in enumerate(lines):
        turns = game.strip().split(": ")[1].split("; ")
        for turn in turns:
            m = {"red":0,"green":0,"blue":0}
            for color in turn.split(", "):
                num,col = color.split()
                m[col] = int(num)
            if m["red"] > 12 or m["green"] > 13 or m["blue"] > 14:
                break
        else:
            total += id + 1
    
    return total

def part_two(lines):
    total = 0
    for _, game in enumerate(lines):
        turns = game.strip().split(": ")[1].split("; ")
        mincubes = {"red":0,"green":0,"blue":0}
        for turn in turns:
            for color in turn.split(", "):
                num,col = color.split()
                if mincubes[col] < int(num):
                    mincubes[col] = int(num)

        total += mincubes["red"] * mincubes["green"] * mincubes["blue"]
    return total

if __name__ =="__main__":
    with open(file="input.txt") as f:
        lines = f.read().splitlines()

    print(part_one(lines))
    print(part_two(lines))