def part_one(grid):
    cs = set()
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch.isdigit() or ch == ".":
                continue
            for cr in [r-1,r,r+1]:
                for cc in [c-1,c,c+1]:
                    if cr < 0 or cr >= len(grid) or cc < 0 or cc >= len(grid[cr]) or not grid[cr][cc].isdigit():
                        continue
                    while cc > 0 and grid[cr][cc-1].isdigit():
                        cc -= 1
                    cs.add((cr,cc))
    
    numbers = []

    for r,c in cs:
        s = ""
        while c < len(grid[r]) and grid[r][c].isdigit():
            s += grid[r][c]
            c += 1
        numbers.append(int(s))
    return sum(numbers)



def part_two(grid):
    total = 0
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch != "*":
                continue
            
            cs = set()
            for cr in [r-1,r,r+1]:
                for cc in [c-1,c,c+1]:
                    if cr < 0 or cr >= len(grid) or cc < 0 or cc >= len(grid[cr]) or not grid[cr][cc].isdigit():
                        continue
                    while cc > 0 and grid[cr][cc-1].isdigit():
                        cc -= 1
                    cs.add((cr,cc))

            if len(cs) != 2:
                continue
            numbers = []

            for cr,cc in cs:
                s = ""
                while cc < len(grid[cr]) and grid[cr][cc].isdigit():
                    s += grid[cr][cc]
                    cc += 1
                numbers.append(int(s))

            total += numbers[0] * numbers[1]
    return total

if __name__ == "__main__":
    with open(file="d3input.txt") as f:
        grid = f.read().splitlines()
    print(part_one(grid))
    print(part_two(grid))