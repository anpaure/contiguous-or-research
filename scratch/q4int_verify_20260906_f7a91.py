"""Independent integer-only checker for explicit [4]^6 chain-pair covers."""

import argparse
from collections import Counter
from hashlib import sha256
from itertools import product
import json
from pathlib import Path


DUAL12 = {
    (0, 2, 4, 0): 12, (0, 3, 1, 2): 6, (0, 3, 2, 1): 10,
    (0, 3, 3, 0): 6, (0, 4, 0, 2): 4, (0, 4, 1, 1): 5,
    (0, 5, 0, 1): 13, (1, 1, 2, 2): 6, (1, 1, 3, 1): 11,
    (1, 2, 0, 3): 12, (1, 2, 1, 2): 5, (1, 2, 2, 1): 4,
    (1, 3, 0, 2): 3, (2, 0, 1, 3): 12, (2, 0, 2, 2): 6,
    (2, 1, 1, 2): 2,
}


def weight12(point):
    counts = tuple(point.count(i) for i in range(4))
    return DUAL12.get(min(counts, counts[::-1]), 0)


def check(data):
    assert data['q'] == 4 and data['dimension'] == 6
    coverage = Counter()
    cost = 0
    slacks = []
    shapes = Counter()
    for row in data['rectangles']:
        left, right = row['left'], row['right']
        c, d = row['C'], row['D']
        assert left and right and sorted(left + right) == list(range(6))
        for axes, chain in ((left, c), (right, d)):
            assert chain
            assert all(len(p) == len(axes) and all(type(x) is int and 0 <= x < 4 for x in p)
                       for p in chain)
            assert all(a != b and all(x <= y for x, y in zip(a, b))
                       for a, b in zip(chain, chain[1:]))
        dual = 0
        for x, y in product(c, d):
            point = [0] * 6
            for axis, value in zip(left + right, x + y):
                point[axis] = value
            point = tuple(point)
            coverage[point] += 1
            dual += weight12(point)
        charge = len(c) + len(d)
        cost += charge
        assert dual <= 12 * charge
        slacks.append(12 * charge - dual)
        shapes[(len(left), len(c), len(d))] += 1
    full = set(product(range(4), repeat=6))
    assert set(coverage) == full, f'missing {len(full - set(coverage))} targets'
    assert type(data['cost']) is int and cost == data['cost']
    dual_overlap12 = sum((count - 1) * weight12(point) for point, count in coverage.items())
    assert sum(slacks) + dual_overlap12 == 12 * (cost - 1248)
    result = {
        'cost': cost, 'rectangles': len(data['rectangles']), 'targets': len(coverage),
        'volume': sum(coverage.values()), 'excess': sum(coverage.values()) - 4096,
        'multiplicity_histogram': dict(sorted(Counter(coverage.values()).items())),
        'dual_slack12': sum(slacks), 'dual_overlap12': dual_overlap12,
        'shape_counts': {str(k): v for k, v in sorted(shapes.items())},
    }
    print(json.dumps(result, sort_keys=True), flush=True)
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('witness')
    args = parser.parse_args()
    raw = Path(args.witness).read_bytes()
    result = check(json.loads(raw))
    print(f'PASS independent explicit integral witness; sha256={sha256(raw).hexdigest()}')
