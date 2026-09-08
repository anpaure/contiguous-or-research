import sys


def g(x, m):
    before = []
    height = d0 = 0
    for i in range(2 * m):
        before.append(height)
        if not (x >> i) & 1 and height == 0:
            d0 += 1
        height += 1 if (x >> i) & 1 else -1
    seen = 0
    for i in range(2 * m):
        if not (x >> i) & 1 and before[i] in (0, 1):
            seen += 1
            if seen == d0 + 1:
                return x | (1 << i), i
    raise AssertionError


def hmap(y, m):
    before = []
    height = u1 = 0
    for i in range(2 * m):
        before.append(height)
        if (y >> i) & 1 and height == 1:
            u1 += 1
        height += 1 if (y >> i) & 1 else -1
    seen = 0
    for i in range(2 * m):
        if (y >> i) & 1 and before[i] in (0, 1):
            seen += 1
            if seen == u1:
                return y & ~(1 << i), i
    raise AssertionError


def tight(word):
    m = len(word) // 2
    x = sum((bit == "1") << i for i, bit in enumerate(word))
    omitted = []
    for _ in range(m):
        y, a = g(x, m)
        x, b = hmap(y, m)
        omitted.extend((a, b))
    omitted.append(2 * m)
    n = 2 * m + 1
    return [omitted[(2 * j) % n] for j in range(n)]


def states(order, d):
    n = len(order)
    s = (n + 1) // 2 - d
    for orientation in range(2):
        row = order if orientation == 0 else list(reversed(order))
        for shift in range(n):
            maximal = []
            forced = []
            for j in range(d):
                window = [row[(shift + j + z) % n] for z in range(s)]
                maximal.append(set(window))
                forced.append({window[0], window[-1]})
            yield orientation, shift, maximal, forced


def main():
    d = int(sys.argv[1])
    words = sys.argv[2:]
    orders = [tight(word) for word in words]
    print("orders", *orders, sep="\n")
    for left in states(orders[0], d):
        for right in states(orders[1], d):
            if all((left[3][j] | right[3][j]) <=
                   (left[2][j] & right[2][j]) for j in range(d)):
                print("witness", left[:2], right[:2])
                for j in range(d):
                    print(j, "P", sorted(left[2][j]), sorted(right[2][j]),
                          "F", sorted(left[3][j]), sorted(right[3][j]),
                          "intersection", sorted(left[2][j] & right[2][j]))
                return
    print("NO WITNESS")


if __name__ == "__main__":
    main()
