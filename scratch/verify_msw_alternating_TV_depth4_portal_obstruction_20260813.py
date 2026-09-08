#!/usr/bin/env python3
"""Formula verifier for the all-m T0(10)^s depth-four portal obstruction.

This uses only the explicit owner-order formulas, never enumerating the MSW
factor.  Broad ranges should be run on h100 by project policy.
"""

from __future__ import annotations

import argparse
import collections
import json


CORE = {0, 1, 4, 5, 8, 9, 10, 11}


def root_word(m, x):
    fixed = {
        0: "101100110010",
        1: "111100110000",
        4: "110110110000",
        5: "110101110000",
        8: "110110011000",
        9: "110110010100",
        10: "110111010000",
        11: "110110010010",
    }
    if x in fixed:
        word = fixed[x] + "10" * (m - 6)
    else:
        assert 12 <= x <= 2 * m - 2 and x % 2 == 0
        i = (x - 12) // 2
        word = ("110110010011" + "10" * i + "00"
                + "10" * (m - 7 - i))
    assert len(word) == 2 * m
    height = 0
    for bit in word:
        height += 1 if bit == "1" else -1
        assert height >= 0
    assert height == 0
    return word


def tight_order(root):
    """Exact canonical g/h construction, used only as provenance replay."""
    m = len(root) // 2
    state = sum((bit == "1") << i for i, bit in enumerate(root))
    omitted = []
    for _ in range(m):
        before, height, d0 = [], 0, 0
        for i in range(2 * m):
            before.append(height)
            if not ((state >> i) & 1) and height == 0:
                d0 += 1
            height += 1 if ((state >> i) & 1) else -1
        seen = 0
        for i in range(2 * m):
            if (not ((state >> i) & 1) and before[i] in (0, 1)):
                seen += 1
                if seen == d0 + 1:
                    state |= 1 << i
                    omitted.append(i)
                    break
        else:
            raise AssertionError("g failed")

        before, height, u1 = [], 0, 0
        for i in range(2 * m):
            before.append(height)
            if ((state >> i) & 1) and height == 1:
                u1 += 1
            height += 1 if ((state >> i) & 1) else -1
        seen = 0
        for i in range(2 * m):
            if ((state >> i) & 1) and before[i] in (0, 1):
                seen += 1
                if seen == u1:
                    state &= ~(1 << i)
                    omitted.append(i)
                    break
        else:
            raise AssertionError("h failed")
    omitted.append(2 * m)
    n = 2 * m + 1
    return [omitted[(2 * j) % n] for j in range(n)]


def is_oriented_cyclic_interval(order, interval):
    n, r = len(order), len(interval)
    for candidate in (order, order[::-1]):
        for start in range(n):
            if all(candidate[(start + j) % n] == interval[j]
                   for j in range(r)):
                return True
    return False


def owner_word(m, x):
    E = list(range(12, 2 * m - 1, 2))
    Ed = E[::-1]
    fixed = {
        0: [10] + E + [1, 5, 4, 9, 8, 11],
        1: [10, 8, 9, 4, 5, 11] + Ed + [0],
        4: [10, 8, 9, 5, 11] + Ed + [0, 1],
        5: [4, 10, 8, 9, 11] + Ed + [0, 1],
        8: [5, 10, 9, 11] + Ed + [0, 1, 4],
        9: [5, 8, 10, 11] + Ed + [0, 1, 4],
        10: [8, 9, 11] + Ed + [0, 1, 4, 5],
        11: [5, 8, 9] + Ed + [10, 0, 1, 4],
    }
    if x in fixed:
        word = fixed[x]
    else:
        assert x in E
        word = ([5, 8, 9] + sorted((e for e in E if e > x), reverse=True)
                + [10] + sorted((e for e in E if e < x), reverse=True)
                + [11, 0, 1, 4])
    U = CORE | set(E)
    assert len(word) == m + 1 and set(word) == U - {x}
    return word


def port_state(word, side, reverse):
    if reverse:
        word = word[::-1]
    R = len(word)
    s = R - 4
    offset = int(side == "L")
    maximal, forced = [], []
    for j in range(4):
        start = offset + j
        p = set(word[start:start + s])
        maximal.append(p)
        forced.append({word[start], word[start + s - 1]})
    return maximal, forced


def bad_coordinates(a, b):
    ma, fa = a
    mb, fb = b
    ans = set()
    for j in range(4):
        ans |= (fa[j] | fb[j]) - (ma[j] & mb[j])
    return ans


def audit(m):
    E = list(range(12, 2 * m - 1, 2))
    U = sorted(CORE | set(E))
    for x in U:
        row = tight_order(root_word(m, x))
        assert is_oriented_cyclic_interval(row, owner_word(m, x))
    incompatible = 0
    core_survivors = []
    for x in U:
        for y in U:
            if x == y:
                continue
            for rx in (False, True):
                for ry in (False, True):
                    left = port_state(owner_word(m, x), "L", rx)
                    right = port_state(owner_word(m, y), "R", ry)
                    bad = bad_coordinates(left, right)
                    assert bad
                    incompatible += 1
                    if not bad & CORE:
                        core_survivors.append((x, y, int(rx), int(ry),
                                               tuple(sorted(bad))))
    # Up to swapping the two seam sides and reversing both circuits, the
    # only core-projection survivors have the displayed form.
    normalized = set()
    for x, y, rx, ry, bad in core_survivors:
        if x == 10 and y in E and rx == ry:
            normalized.add((y, bad))
        elif y == 10 and x in E and rx == ry:
            normalized.add((x, bad))
        else:
            raise AssertionError((m, x, y, rx, ry, bad))
    expected_y = E[:-2]
    assert sorted(y for y, _ in normalized) == expected_y
    emax = E[-1]
    assert all(emax in bad for _, bad in normalized)
    return {
        "m": m,
        "owners": len(U),
        "canonical_root_provenance": True,
        "ordered_cross_port_modes": incompatible,
        "core_projection_survivors_before_symmetry": len(core_survivors),
        "normalized_survivor_missing_labels": expected_y,
        "final_tail_witness": emax,
        "pass": True,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("m_max", type=int)
    ap.add_argument("--m-min", type=int, default=8)
    ap.add_argument("--json")
    args = ap.parse_args()
    ans = [audit(m) for m in range(args.m_min, args.m_max + 1)]
    payload = json.dumps(ans, indent=2, sort_keys=True)
    print(payload)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            f.write(payload + "\n")


if __name__ == "__main__":
    main()
