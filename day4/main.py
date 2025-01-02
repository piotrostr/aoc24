sample = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

print("total Xs:", sample.count("X"))


# switch case would be faster
def get_next_char(char: str) -> str:
    xmas = "XMAS"
    return xmas[(xmas.find(char) + 1) % len(xmas)]


def sample_to_matrix(sample: str) -> list[list[str]]:
    rows = [row for row in sample.splitlines() if row]
    m = [["" for _ in range(len(rows))] for _ in range(len(rows))]
    for y in range(len(rows)):
        for x in range(len(rows[y])):
            m[y][x] = rows[y][x]

    return m


def check_bounds(m: list[list[str]], point: tuple[int, int]) -> bool:
    if 0 <= point[0] < len(m) and 0 <= point[1] < len(m[0]):
        return True
    return False


def get_neighbors(m: list[list[str]], point: tuple[int, int]) -> list[tuple[int, int]]:
    neighbors = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    for dy, dx in directions:
        neighbor = (point[0] + dy, point[1] + dx)
        if check_bounds(m, neighbor):
            neighbors.append(neighbor)

    return neighbors


def find_xmases(m: list[list[str]]) -> tuple[list[list[str]], int]:
    xs = []
    for y in range(len(m)):
        for x in range(len(m[y])):
            if m[y][x] == "X":
                xs.append((y, x))

    xmases_count = 0
    for yx, xx in xs:
        stack = [(yx, xx, [(yx, xx)])]
        while len(stack) > 0:
            y, x, path = stack.pop()
            if len(path) == 4:
                if [m[y][x] for y, x in path] == ["X", "M", "A", "S"]:
                    xmases_count += 1
                continue
            current_char = m[y][x]
            next_char = get_next_char(current_char)

            neighbors = get_neighbors(m, (y, x))
            for ny, nx in neighbors:
                if m[ny][nx] == next_char and (ny, nx) not in path:
                    new_path = path + [(ny, nx)]
                    stack.append((ny, nx, new_path))

    return ([], xmases_count)


if __name__ == "__main__":
    m = sample_to_matrix(sample)
    print(find_xmases(m))
    # with open("input.txt") as f:
    #     contents = f.read()
