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


def count_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # All possible directions: right, down, diagonal-right-down, diagonal-left-down
    # and their reverses for "SAMX"
    directions = [
        (0, 1),  # right
        (1, 0),  # down
        (1, 1),  # diagonal right-down
        (1, -1),  # diagonal left-down
    ]

    def check_word(x, y, dx, dy):
        # Check both "XMAS" and "SAMX"
        words = ["XMAS", "SAMX"]

        for word in words:
            if not (
                0 <= x + (len(word) - 1) * dx < rows
                and 0 <= y + (len(word) - 1) * dy < cols
            ):
                continue

            found = True
            for i in range(len(word)):
                if grid[x + i * dx][y + i * dy] != word[i]:
                    found = False
                    break
            if found:
                return 1
        return 0

    # Check each starting position
    for i in range(rows):
        for j in range(cols):
            # Try each direction
            for dx, dy in directions:
                count += check_word(i, j, dx, dy)

    return count


# Read input
grid = []
with open("input.txt", "r") as f:
    for line in f:
        grid.append(line.strip())

# Get result
result = count_xmas(grid)
# sample.strip().split("\n"))
print(f"XMAS appears {result} times")
