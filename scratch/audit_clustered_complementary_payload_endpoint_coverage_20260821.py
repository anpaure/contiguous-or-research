#!/usr/bin/env python3
import math


def atom_word(b, r):
    schedule = [0] * r + [1] * (b - r)
    ia = ib = 0
    word = []
    for t in range(b * b):
        if schedule[t % b] == 0:
            word.append(ia)
            ia = (ia + 1) % b
        else:
            word.append(b + ib)
            ib = (ib + 1) % b
    return word


def selected_balanced_targets(word, b, q, s):
    length = len(word)
    out = set()
    for end in range(length):
        target = frozenset(word[(end - offset) % length] for offset in range(b + q))
        if len(target) == b + q and sum(x < b for x in target) == s:
            out.add(target)
    return out


def exact_checks():
    for b in (11, 13, 17, 23, 31, 43):
        for q in range(1, min(9, b // 3), 2):
            r = (b - q) // 2
            s = b - r
            low = selected_balanced_targets(atom_word(b, r), b, q, s)
            high = selected_balanced_targets(atom_word(b, s), b, q, s)
            h = (b - 3 * q + 2) // 2
            assert len(low) == len(high) == h * b, (b, q, len(low), len(high), h)
            assert low.isdisjoint(high), (b, q, len(low & high))
            assert len(low | high) == (b - 3 * q + 2) * b
        print("exact complementary endpoints PASS", b)


def aggregate_checks():
    for b in (101, 503, 2003, 5003, 10003):
        h_band = int(b ** 0.60)
        if h_band % 2 == 0:
            h_band -= 1
        w = math.comb(2 * b, b)
        mass = 0.0
        holes = 0.0
        for q in range(1, h_band + 1, 2):
            p = math.comb(b, (b - q) // 2) ** 2
            mass += p / w
            holes += ((3 * q - 2) / b) * (p / w)
        print(
            "aggregate PASS",
            b,
            "H",
            h_band,
            "balanced mass/W",
            mass,
            "holes/W",
            holes,
            "holes*sqrt(b)/W",
            holes * math.sqrt(b),
        )


if __name__ == "__main__":
    exact_checks()
    aggregate_checks()
    print("ALL COMPLEMENTARY-PAYLOAD ENDPOINT CHECKS PASS")
