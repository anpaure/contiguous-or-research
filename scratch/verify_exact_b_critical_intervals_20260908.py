"""Read-only finite audit; execute only on h100, never on the Mac."""
from collections import Counter
from math import comb
from pathlib import Path
import json
import sys


def audit(path, k):
    word = [int(s, 0) for s in path.read_text().split()]
    n = len(word)
    r = (k + 1) // 2
    width = comb(k, r)
    lower = sum(comb(k, s) for s in range(1, r))
    depth = 0
    while depth * width + depth * (depth + 1) // 2 < lower:
        depth += 1
    assert n == width + depth
    slack = depth * width + depth * (depth + 1) // 2 - lower
    bits = [[b for b in range(k) if a >> b & 1] for a in word]
    counts = [0] * k
    rank = 0
    end = 0
    candidates = []
    lower_cells = 0
    for start in range(n):
        while end < n and rank < r:
            for b in bits[end]:
                if counts[b] == 0:
                    rank += 1
                counts[b] += 1
            end += 1
        if rank >= r:
            label = sum(1 << b for b, c in enumerate(counts) if c)
            candidate = (start, end - 1, label)
            if candidates and candidates[-1][1] == end - 1:
                candidates[-1] = candidate
            else:
                candidates.append(candidate)
            lower_cells += end - start - 1
        else:
            lower_cells += n - start
        for b in bits[start]:
            counts[b] -= 1
            if counts[b] == 0:
                rank -= 1

    p = len(candidates)
    q = n - p
    assert width <= p <= width + 1
    assert lower <= lower_cells <= q * n - q * (q - 1) // 2
    assert (p * (p + 1) - width * (width + 1)) // 2 <= slack
    labels = Counter(label for _, _, label in candidates)
    if slack < width + 1:
        assert p == width
        assert len(labels) == width
        assert all(label.bit_count() == r for label in labels)

    suffixes = set()
    last_seen = {}
    for j, a in enumerate(word):
        suffixes = {a} | {a | old for old in suffixes}
        middle = [s for s in suffixes if s.bit_count() == r]
        assert len(middle) <= 1
        if middle:
            target = middle[0]
            if slack < width + 1 and target in last_seen:
                assert last_seen[target] == j - 1
            last_seen[target] = j
    assert len(last_seen) == width
    return dict(k=k, n=n, r=r, W=width, d=depth, sigma=slack,
                critical_intervals=p, lower_cells=lower_cells,
                distinct_critical_labels=len(labels), passed=True)


root = Path(sys.argv[1])
records = [audit(root / f"k{k:02}.word", k) for k in range(1, 17)]
print(json.dumps(records, indent=2))
