"""Independent full-word last-occurrence audit; writes no output files.

With --binary, runs the search, captures its emitted seed, and audits the
entire developed word without orbit compression or incremental profiles.
"""

import argparse
import hashlib
import subprocess
import sys
from array import array
from math import comb


CERTIFICATES = [
    (7, [3, 5, 64, 20, 36], [0] * 7),
    (9, [1, 130, 136, 12, 36, 48, 80, 272, 18, 17, 9, 65, 96, 68],
     [0, 0, 0, 0, 9, 3, 0, 0, 0]),
    (9, [44, 134, 6, 68, 28, 16, 36, 360, 168, 137, 76, 145, 146, 10],
     [0, 0, 0, 72, 63, 0, 0, 0, 0]),
    (11, [1072, 1152, 1042, 8, 1296, 1792, 1600, 1089, 1152, 66, 162,
          146, 17, 259, 7, 69, 577, 97, 320, 273, 280, 26, 20, 38, 1056,
          1538, 8, 1284, 772, 384, 641, 704, 656, 644, 1664, 129, 1033,
          1034, 1048, 1536, 1096, 73],
     [0, 0, 0, 11, 22, 33, 11, 0, 0, 0, 0]),
    (13, [2066, 66, 2562, 643, 650, 4248, 648, 1048, 1200, 1312, 20,
          3328, 2310, 2370, 322, 768, 386, 4362, 4356, 263, 1284, 1093,
          1121, 3392, 5184, 7172, 2084, 4224, 2209, 64, 2224, 1168, 672,
          1196, 96, 174, 4136, 14, 2054, 1024, 2051, 257, 34, 4096, 515,
          521, 13, 260, 1288, 296, 4128, 800, 2560, 2432, 4288, 464,
          146, 387, 267, 4361, 4617, 4737, 577, 4101, 6212, 20, 6416,
          4368, 18, 5122, 1154, 642, 576, 132, 2116, 2069, 277, 48, 294,
          4098, 4644, 4612, 640, 192, 4352, 328, 24, 112, 34, 194, 129,
          2240, 3200, 1028, 6148, 4116, 4624, 24, 529, 33, 180, 304,
          292, 258, 2054, 2692, 2049, 4224, 5125, 4102, 1092, 578,
          1632, 1184, 1540, 3584, 2848, 40, 4353, 4109, 72, 4166, 132,
          5120, 1344, 960, 2752, 2561, 2193, 2097, 4145, 257],
     [0, 0, 0, 0, 39, 182, 247, 78, 0, 0, 0, 0, 0]),
    (13, [1088, 5385, 4482, 400, 2288, 4120, 65, 3140, 2080, 6160,
          2180, 5920, 4374, 5644, 842, 2896, 3346, 6920, 2078, 2077,
          2436, 2676, 2252, 6752, 3332, 2049, 4163, 5194, 1682, 4124,
          1222, 93, 1035, 1097, 264, 517, 1537, 3073, 33, 5122, 4192,
          5440, 5128, 768, 516, 3, 4105, 4, 40, 5120, 3104, 2592, 2624,
          528, 80, 144, 2, 272, 136, 2057, 6145, 512, 336, 274, 6256,
          297, 6400, 7176, 5124, 1104, 5122, 4290, 4674, 322, 4417,
          4361, 18, 2321, 440, 3210, 5133, 6532, 4769, 5154, 1801,
          4401, 299, 5146, 1152, 2180, 1, 2178, 2080, 18, 2560, 4624,
          4120, 4100, 4113, 33, 2562, 768, 612, 4704, 707, 1121, 2112,
          354, 433, 4754, 3122, 47, 2689, 544, 2566, 6146, 5138, 1, 28,
          4116, 5124, 140, 266, 386, 1026, 3328, 2560, 576, 1026, 1089,
          4, 4113],
     [0, 0, 0, 0, 0, 1027, 923, 0, 0, 0, 0, 0, 0]),
]


def rotate(x, k, shift):
    shift %= k
    full = (1 << k) - 1
    return ((x << shift) & full) | (x >> (k - shift)) if shift else x


def digest(values):
    packed = array("I", values)
    assert packed.itemsize == 4
    if sys.byteorder != "little":
        packed.byteswap()
    return hashlib.sha256(packed.tobytes()).hexdigest()


def audit(k, seed, expected, brute=False):
    word = [rotate(x, k, shift) for shift in range(k) for x in seed]
    n = len(word)
    assert n == comb(k, k // 2)
    assert all(0 < x < (1 << k) for x in word)
    last = [-1] * k
    for i, letter in enumerate(word):
        while letter:
            bit = letter & -letter
            last[bit.bit_length() - 1] = i
            letter ^= bit
    assert min(last) >= 0
    seen = bytearray(1 << k)
    for i, letter in enumerate(word, n):
        while letter:
            bit = letter & -letter
            last[bit.bit_length() - 1] = i
            letter ^= bit
        order = sorted(range(k), key=last.__getitem__, reverse=True)
        value = 0
        for j, bit in enumerate(order):
            value |= 1 << bit
            if j == k - 1 or last[bit] != last[order[j + 1]]:
                seen[value] = 1
    by_rank = [0] * k
    for x in range(1, 1 << k):
        if not seen[x]:
            by_rank[x.bit_count() - 1] += 1
    assert by_rank == expected, (k, by_rank, expected)
    if brute:
        direct = bytearray(1 << k)
        for start in range(n):
            value = 0
            for width in range(n):
                value |= word[(start + width) % n]
                direct[value] = 1
        assert direct == seen
    print("INDEPENDENT_PASS", {"k": k, "period": n, "holes": sum(by_rank),
                               "density": sum(by_rank) / (1 << k),
                               "holes_over_width": sum(by_rank) / n,
                               "ranks": by_rank, "seed_sha256_le32": digest(seed),
                               "word_sha256_le32": digest(word)}, flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--binary")
    parser.add_argument("--k", type=int, default=23)
    parser.add_argument("--steps", type=int, default=8000000)
    parser.add_argument("--rounds", type=int, default=8)
    parser.add_argument("--seed", type=int, default=9064476)
    parser.add_argument("--ignore-middle-pairs", type=int, default=0)
    args = parser.parse_args()
    if not args.binary:
        for k, seed, expected in CERTIFICATES:
            audit(k, seed, expected, brute=True)
        print("SMALL_CERTIFICATES_PASS", len(CERTIFICATES))
        return
    command = [args.binary, "--k", str(args.k), "--steps", str(args.steps),
               "--rounds", str(args.rounds), "--seed", str(args.seed),
               "--ignore-middle-pairs", str(args.ignore_middle_pairs), "--emit"]
    seed = expected = None
    with subprocess.Popen(command, stdout=subprocess.PIPE, text=True) as process:
        for line in process.stdout:
            if line.startswith("SEED "):
                seed = [int(x) for x in line.split()[1:]]
            else:
                print(line, end="", flush=True)
                if line.startswith("FINAL "):
                    expected = [int(x) for x in line.split("ranks=", 1)[1].strip().split(",")]
        assert process.wait() == 0
    assert seed is not None and expected is not None
    audit(args.k, seed, expected)


if __name__ == "__main__":
    main()
