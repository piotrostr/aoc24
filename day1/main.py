from collections import Counter

if __name__ == "__main__":
    with open("./input.txt", "r+") as f:
        contents = f.read()

    lines = contents.splitlines()

    l1, l2 = [], []
    for line in lines:
        i1, i2 = line.split("   ")
        l1.append(int(i1))
        l2.append(int(i2))

    l1.sort()
    l2.sort()
    distances = sum([abs(i1 - i2) for (i1, i2) in zip(l1, l2)])

    print(distances)

    counts = Counter(l2)

    res = 0
    for num in l1:
        if num in counts:
            res += num * counts[num]

    print(res)
