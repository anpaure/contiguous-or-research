#!/usr/bin/env python3
"""Finite checks for MATH_THEOREM_CONSTANT_ORIGIN_ENDPOINT_PROFILE_CAPACITY."""

import math


def exact_deficit(b: int):
    h = math.ceil(math.sqrt(b * math.log(b)))
    w = math.comb(2 * b, b)
    total_num = 0
    per_q = []
    for q in range(1, h + 1):
        dq_num = 0
        for s in range(q, b + 1):
            p = math.comb(b, s) * math.comb(b, s - q)
            e_num = 0
            n_b = b - s - h + 1
            n_a = s - q - h + 1
            if n_b > 0:
                e_num += n_b * math.comb(b, s) ** 2
            if n_a > 0:
                e_num += n_a * math.comb(b, s - q) ** 2
            dq_num += max(0, b * p - e_num)
        total_num += dq_num
        per_q.append(dq_num)
    return h, total_num / (b * w), max(per_q) / (b * w)


def check_ratio_identity(b: int):
    h = math.ceil(math.sqrt(b * math.log(b)))
    for q in range(1, min(h, b // 4) + 1):
        for s in range(max(q, b // 4), min(b, 3 * b // 4) + 1):
            if not (b // 4 <= s - q <= 3 * b // 4):
                continue
            p = math.comb(b, s) * math.comb(b, s - q)
            e_num = (
                (b - s - h + 1) * math.comb(b, s) ** 2
                + (s - q - h + 1) * math.comb(b, s - q) ** 2
            )
            x = s - (b + q) / 2
            a = (b - q) / 2 - h + 1
            r = math.comb(b, s) / math.comb(b, s - q)
            rhs = ((a - x) * r + (a + x) / r)
            assert abs(e_num / p - rhs) <= 1e-8 * max(1.0, abs(rhs))


def main():
    for b in (31, 43, 61, 101, 151, 251, 503):
        check_ratio_identity(b)
        h, total, mx = exact_deficit(b)
        print(f"b={b:4d} H={h:3d} total/W={total:.12f} maxq/W={mx:.12f}")
    print("PASS")


if __name__ == "__main__":
    main()
