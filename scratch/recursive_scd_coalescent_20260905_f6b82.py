"""Exact recursive SCD compiler checks; no numerical limit is inferred."""

from functools import lru_cache
from itertools import combinations, product
from math import prod
from collections import Counter

from density_bridge_frontier_20260905_c71e4 import bridge, scd, unions
from four_block_cross_split_20260905_d29f6 import multiply_chains, width3


@lru_cache(None)
def grid_width(lengths):
    coefficients = [1]
    for length in lengths:
        following = [0] * (len(coefficients) + length - 1)
        for i, value in enumerate(coefficients):
            for j in range(length):
                following[i + j] += value
        coefficients = following
    return max(coefficients)


def one_split_cost(lengths):
    size = len(lengths)
    best = None
    for mask in range(1, (1 << size) - 1, 2):
        left = tuple(lengths[i] for i in range(size) if mask & (1 << i))
        right = tuple(lengths[i] for i in range(size) if not mask & (1 << i))
        cost = prod(left) * grid_width(right) + prod(right) * grid_width(left)
        best = cost if best is None else min(best, cost)
    return best


@lru_cache(None)
def recursive_cost(lengths):
    lengths = tuple(sorted(lengths))
    if len(lengths) == 2:
        return sum(lengths)
    best = None
    considered = set()
    for i, j in combinations(range(len(lengths)), 2):
        a, b = lengths[i], lengths[j]
        if (a, b) in considered:
            continue
        considered.add((a, b))
        rest = tuple(lengths[t] for t in range(len(lengths)) if t not in (i, j))
        cost = sum(recursive_cost(tuple(sorted(rest + (length,))))
                   for length in range(abs(a - b) + 1, a + b, 2))
        best = cost if best is None else min(best, cost)
    return best


def recursive_leaves(factors):
    if len(factors) == 2:
        yield factors
        return
    lengths = tuple(sorted(len(chain) for _, chain in factors))
    target = recursive_cost(lengths)
    for i, j in combinations(range(len(factors)), 2):
        a, b = len(factors[i][1]), len(factors[j][1])
        rest = [factor for t, factor in enumerate(factors) if t not in (i, j)]
        rest_lengths = tuple(len(chain) for _, chain in rest)
        cost = sum(recursive_cost(tuple(sorted(rest_lengths + (length,))))
                   for length in range(abs(a - b) + 1, a + b, 2))
        if cost == target:
            support = factors[i][0] | factors[j][0]
            for chain in multiply_chains(factors[i][1], factors[j][1]):
                yield from recursive_leaves(rest + [(support, tuple(chain))])
            return
    raise AssertionError("The finite dynamic-programming minimizer was not found")


def compile_cube(block_sizes):
    universes = []
    decompositions = []
    offset = 0
    for size in block_sizes:
        universes.append(((1 << size) - 1) << offset)
        decompositions.append(scd([1 << i for i in range(offset, offset + size - 1)]))
        offset += size
    full = (1 << offset) - 1
    adjacency = {}
    edges = set()
    partition = set()
    main_cost = 0
    dp_cost = 0
    for chains in product(*decompositions):
        dp_cost += (1 << (len(chains) - 1)) * recursive_cost(tuple(sorted(map(len, chains))))
        for signs in product((0, 1), repeat=len(chains) - 1):
            factors = [(u, tuple(c) if s == 0 else tuple(u ^ x for x in reversed(c)))
                       for u, c, s in zip(universes, chains, (0,) + signs)]
            for leaf in recursive_leaves(factors):
                left, right = leaf
                if not (left[0] & universes[0]):
                    left, right = right, left
                desired_right = right[1]
                right = (right[0], tuple(right[0] ^ x for x in reversed(right[1])))
                edge = (left, right)
                assert edge not in edges
                edges.add(edge)
                adjacency.setdefault(left, []).append(right)
                adjacency.setdefault(right, []).append(left)
                main_cost += len(left[1]) + len(right[1])
                required = {x | y for x in left[1] for y in desired_right}
                required |= {full ^ x for x in tuple(required)}
                assert not (partition & required)
                partition.update(required)
    assert partition == set(range(full + 1))
    assert main_cost == dp_cost
    word = []
    components = 0
    primary = 0
    seam = 0
    for root in list(adjacency):
        if not adjacency[root]:
            continue
        stack = [root]
        reversed_circuit = []
        while stack:
            if adjacency[stack[-1]]:
                stack.append(adjacency[stack[-1]].pop())
            else:
                reversed_circuit.append(stack.pop())
        circuit = reversed_circuit[::-1]
        assert circuit[0] == circuit[-1]
        for vertex in circuit[:-1]:
            letters = bridge(vertex[1], vertex[0])
            word.extend(letters)
            primary += len(letters)
        letters = bridge(root[1], root[0])
        word.extend(letters)
        seam += len(letters)
        components += 1
    assert abs(primary - main_cost) <= 2 * len(edges)
    assert seam <= (offset + 1) * components
    assert len(word) == primary + seam
    assert unions(word) == set(range(1, full + 1))
    return len(word), main_cost, len(edges), len(adjacency), components


def five_equal_policy(length):
    total = 0
    for child in range(1, 2 * length, 2):
        a, b, c, d = sorted((child, length, length, length))
        total += a * b * c + d * width3(a, b, c)
    return total


@lru_cache(None)
def final_chain_histogram(lengths):
    if len(lengths) == 2:
        a, b = lengths
        return tuple((r, 1) for r in range(abs(a - b) + 1, a + b, 2))
    target = recursive_cost(lengths)
    for i, j in combinations(range(len(lengths)), 2):
        a, b = lengths[i], lengths[j]
        rest = tuple(lengths[t] for t in range(len(lengths)) if t not in (i, j))
        children = [tuple(sorted(rest + (r,)))
                    for r in range(abs(a - b) + 1, a + b, 2)]
        if sum(recursive_cost(child) for child in children) == target:
            total = Counter()
            for child in children:
                total.update(dict(final_chain_histogram(child)))
            return tuple(sorted(total.items()))
    raise AssertionError("Missing optimal merge")


def audit_rank_histograms():
    checked = 0
    for d in (3, 4, 5):
        for lengths in product(range(1, 5), repeat=d):
            coefficients = [1]
            for a in lengths:
                following = [0] * (len(coefficients) + a - 1)
                for i, count in enumerate(coefficients):
                    for j in range(a):
                        following[i + j] += count
                coefficients = following
            height = len(coefficients) - 1
            expected = {}
            previous = 0
            for rank in range(height // 2 + 1):
                count = coefficients[rank] - previous
                if count:
                    expected[height - 2 * rank + 1] = count
                previous = coefficients[rank]
            assert dict(final_chain_histogram(tuple(sorted(lengths)))) == expected
            checked += 1
    return checked


def main():
    print("Exact globally Euler-assembled recursive words:")
    for sizes in ((2, 2, 2), (2, 2, 2, 2), (2, 2, 2, 2, 2),
                  (2, 3, 2, 3), (3, 3, 3, 3), (2, 2, 3, 2, 2)):
        n, cost, edges, vertices, components = compile_cube(sizes)
        print(f"  blocks={sizes}: n={n}, main={cost}, leaves={edges}, vertices={vertices}, components={components}")
    identities = 0
    for a, b in product(range(1, 41), repeat=2):
        children = list(range(abs(a - b) + 1, a + b, 2))
        assert sum(children) == a * b
        assert sum(r * (r*r - 1) for r in children) == a * b * (a*a + b*b - 2)
        identities += 1
    print(f"Exact volume and energy identities checked: {identities}")
    print(f"Adaptive final-chain histograms checked against complete rank polynomials: {audit_rank_histograms()}")
    print("Five-equal-chain constructive improvement (normalized principal costs):")
    for length in (2, 4, 8, 16, 32, 64):
        single = one_split_cost((length,) * 5)
        refined = five_equal_policy(length)
        assert refined < single
        print(f"  L={length}: one split={single/length**4:.12f}, recursive policy={refined/length**4:.12f}")
    print("  proved limits: 5/3 versus 73/48, a gap of 7/48")
    print(f"Dynamic-programming cache: {recursive_cost.cache_info()}")


if __name__ == "__main__":
    main()
