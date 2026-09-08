"""Four-chain cross-hook covers: exact words and numerical diagnostics.

The exact checks use only the standard library. Numerical sampling is not a
certificate for an asymptotic constant.
"""

import argparse
from functools import lru_cache
from itertools import product
from math import comb, pi, sqrt


def hook_chains(a, b, u, v):
    chains = []
    for x in range(a):
        for y in range(b):
            if x < u and y >= v:
                continue
            eligible = [i for i, chain in enumerate(chains)
                        if chain[-1][1] <= y]
            if eligible:
                i = max(eligible, key=lambda j: chains[j][-1][1])
                chains[i].append((x, y))
            else:
                chains.append([(x, y)])
    width = max(min(a, v), min(a - u, b))
    volume = a * b - u * (b - v)
    assert len(chains) == width
    assert sum(map(len, chains)) == volume
    assert all(all(x <= xx and y <= yy for (x, y), (xx, yy)
                   in zip(chain, chain[1:])) for chain in chains)
    return chains


def main_cost(lengths, thresholds, order=(0, 1, 2, 3)):
    volumes, widths = [], []
    for i, j in zip(order, order[1:] + order[:1]):
        a, b = lengths[i], lengths[j]
        u, v = thresholds[i], thresholds[j]
        volumes.append(a * b - u * (b - v))
        widths.append(max(min(a, v), min(a - u, b)))
    return sum(volumes[i] * widths[i + 2] + widths[i] * volumes[i + 2]
               for i in range(2))


def balanced_cuts(lengths):
    """Balance three successive hook widths; optimize the remaining quadratic."""
    orders = [(0, 1, 2, 3), (0, 1, 3, 2), (0, 2, 1, 3)]
    for cycle in orders:
        for shift in range(4):
            order = cycle[shift:] + cycle[:shift]
            a, b, c, d = [lengths[i] for i in order]
            p, q = b - a, c - b + a
            delta = d - q
            eta = max(delta, 0)
            lo = max(0, a - b, -delta)
            hi = min(a, q, (a if delta >= 0 else d) - eta)
            if lo > hi:
                continue
            quadratic = min(a + c, b + d)
            linear = ((b - d) * (c - a) + (p - a) * delta
                      - 2 * a * q + (a + q) * eta)
            t = min(hi, max(lo, -linear / (2 * quadratic)))
            local = (t, a - t, p + t, q - t)
            thresholds = [0] * 4
            for i, value in zip(order, local):
                thresholds[i] = value
            yield tuple(thresholds), order


def bridge(chain, support):
    letters = [chain[0]]
    letters.extend(y & ~x for x, y in zip(chain, chain[1:]))
    letters.append(support & ~chain[-1])
    return [x for x in letters if x]


def interval_unions(word):
    all_unions, suffixes = set(), set()
    for letter in word:
        assert letter
        suffixes = {letter} | {x | letter for x in suffixes}
        all_unions.update(suffixes)
    return all_unions


def literal_cover(lengths, thresholds, order=(0, 1, 2, 3)):
    # Each input chain has a private always-present bit and an always-absent
    # bit. Thus its product and full complement are disjoint paired families.
    chains, supports = [], []
    bit = 0
    for a in lengths:
        first = 1 << bit
        bit += 1
        chain = [first]
        support = first
        for _ in range(a - 1):
            support |= 1 << bit
            chain.append(support)
            bit += 1
        support |= 1 << bit
        bit += 1
        chains.append(chain)
        supports.append(support)
    word, charge, edges = assemble_cover(chains, supports, thresholds, order)
    full = sum(supports)
    required = set()
    for choice in product(*chains):
        target = 0
        for x in choice:
            target |= x
        required.update((target, full ^ target))
    assert required <= interval_unions(word)
    return len(word), charge, edges, len(required)


def assemble_cover(chains, supports, thresholds, order=(0, 1, 2, 3)):
    lengths = tuple(map(len, chains))
    word, charge, edges = [], 0, 0
    for shift in (0, 1):
        i, j, k, ell = (order[(shift + q) % 4] for q in range(4))
        left = hook_chains(lengths[i], lengths[j], thresholds[i], thresholds[j])
        right = hook_chains(lengths[k], lengths[ell], thresholds[k], thresholds[ell])
        if not left or not right:
            continue
        left_sets = [[chains[i][x] | chains[j][y] for x, y in c] for c in left]
        right_sets = [[chains[k][x] | chains[ell][y] for x, y in c] for c in right]
        u, v = supports[i] | supports[j], supports[k] | supports[ell]
        for c in left_sets:
            # A row word serves both orientations and pays its closing copy.
            bc = bridge(c, u)
            word.extend(bc)
            for d in right_sets:
                dc = [v ^ x for x in reversed(d)]
                word.extend(bridge(dc, v))
                word.extend(bc)
                charge += len(c) + len(d)
                edges += 1
    assert charge == main_cost(lengths, thresholds, order)
    total = sum(lengths)
    assert len(word) <= charge + total * total + total + 1
    return word, charge, edges


@lru_cache(None)
def finite_choice(lengths):
    best = None
    for thresholds in product(*(range(a + 1) for a in lengths)):
        for order in ((0, 1, 2, 3), (0, 1, 3, 2), (0, 2, 1, 3)):
            item = (main_cost(lengths, thresholds, order), thresholds, order)
            if best is None or item < best:
                best = item
    return best


def full_cube_audit():
    for h in (2, 3, 4):
        supports = [((1 << h) - 1) << (i * h) for i in range(4)]
        scds = []
        for i in range(4):
            chains = [[0]]
            for bit in range(i * h, (i + 1) * h - 1):
                following = []
                for chain in chains:
                    following.append(chain + [chain[-1] | (1 << bit)])
                    if len(chain) > 1:
                        following.append([x | (1 << bit) for x in chain[:-1]])
                chains = following
            assert len(chains) == comb(h - 1, (h - 1) // 2)
            scds.append(chains)
        word, charge = [], 0
        for originals in product(*scds):
            lengths = tuple(map(len, originals))
            principal, thresholds, order = finite_choice(lengths)
            for signs in product((0, 1), repeat=3):
                desired = [chain if sign == 0 else [support ^ x for x in reversed(chain)]
                           for chain, support, sign in zip(originals, supports, (0,) + signs)]
                block, main, _ = assemble_cover(desired, supports, thresholds, order)
                assert main == principal
                word.extend(block)
                charge += main
        assert interval_unions(word) == set(range(1, 1 << (4 * h)))
        print(f"PASS full cube k={4*h}: length={len(word)} principal={charge} "
              f"targets={(1 << (4*h))-1}")


def audit():
    planar = 0
    for a in range(1, 9):
        for b in range(1, 9):
            for u in range(a + 1):
                for v in range(b + 1):
                    hook_chains(a, b, u, v)
                    planar += 1
    covers = 0
    cases = [(2, 2, 2, 2), (3, 3, 3, 3), (2, 3, 4, 5), (1, 2, 3, 4)]
    for lengths in cases:
        choices = [sorted({0, a // 2, a}) for a in lengths]
        for thresholds in product(*choices):
            literal_cover(lengths, thresholds)
            covers += 1
    print(f"PASS: {planar} exact hook chain covers; {covers} literal paired-box words")
    for m in (1, 2, 3, 5):
        result = literal_cover((2 * m,) * 4, (m,) * 4)
        assert result[1] == 12 * m ** 3
        print(f"equal sides={2*m}: length, charge, edges, targets={result}")
    full_cube_audit()


def numerical(samples, divisions, seed, passes):
    import numpy as np

    rng = np.random.default_rng(seed)
    lengths = np.sort(np.linalg.norm(rng.standard_normal((samples, 4, 3)), axis=2), axis=1)
    a, b, c, d = lengths.T
    volume = np.prod(lengths, axis=1)
    baseline = 1 / c + 1 / d - np.maximum(a + b - c, 0) ** 2 / (4 * a * b * c)
    best = baseline.copy()
    pure = np.full(samples, np.inf)
    fractions = np.linspace(0, 1, divisions + 1)
    orders = [(0, 1, 2, 3), (0, 1, 3, 2), (0, 2, 1, 3)]

    def costs(thresholds, order):
        volumes, widths = [], []
        for i, j in zip(order, order[1:] + order[:1]):
            x, y = lengths[:, i], lengths[:, j]
            u, v = thresholds[:, i], thresholds[:, j]
            volumes.append(x * y - u * (y - v))
            widths.append(np.maximum(np.minimum(x, v), np.minimum(x - u, y)))
        return sum(volumes[i] * widths[i + 2] + widths[i] * volumes[i + 2]
                   for i in range(2)) / volume

    for order in orders:
        order_best = np.full(samples, np.inf)
        chosen = lengths / 2
        for fractions4 in product(fractions, repeat=4):
            thresholds = lengths * fractions4
            cost = costs(thresholds, order)
            mask = cost < order_best
            chosen[mask] = thresholds[mask]
            order_best = np.minimum(order_best, cost)
        for _ in range(passes):
            for position, i in enumerate(order):
                previous, following = order[position - 1], order[(position + 1) % 4]
                candidates = [np.zeros(samples), lengths[:, i], lengths[:, previous],
                              lengths[:, i] - lengths[:, following],
                              lengths[:, previous] - chosen[:, previous],
                              lengths[:, i] - chosen[:, following]]
                local = chosen.copy()
                for candidate in candidates:
                    thresholds = chosen.copy()
                    thresholds[:, i] = np.clip(candidate, 0, lengths[:, i])
                    cost = costs(thresholds, order)
                    mask = cost < order_best - 1e-13
                    local[mask] = thresholds[mask]
                    order_best = np.minimum(order_best, cost)
                chosen = local
        pure = np.minimum(pure, order_best)
        best = np.minimum(best, order_best)
    scale = sqrt(pi / 2)
    for name, values in [("baseline", baseline), ("cross-hook", pure), ("hybrid", best)]:
        print(f"{name}: mean={scale*np.mean(values):.10f} "
              f"SE={scale*np.std(values)/sqrt(samples):.10f}")
    print(f"switched fraction={np.mean(pure < baseline):.8f}; "
          f"paired mean saving={scale*np.mean(baseline-best):.10f}")


def numerical_balanced(samples, seed):
    import numpy as np

    rng = np.random.default_rng(seed)
    lengths = np.sort(np.linalg.norm(rng.standard_normal((samples, 4, 3)), axis=2), axis=1)
    a0, b0, c0, d0 = lengths.T
    volume = np.prod(lengths, axis=1)
    baseline = 1 / c0 + 1 / d0 - np.maximum(a0 + b0 - c0, 0) ** 2 / (4 * a0 * b0 * c0)
    best = baseline.copy()
    for cycle in [(0, 1, 2, 3), (0, 1, 3, 2), (0, 2, 1, 3)]:
        for shift in range(4):
            order = cycle[shift:] + cycle[:shift]
            a, b, c, d = [lengths[:, i] for i in order]
            p, q = b - a, c - b + a
            delta = d - q
            eta = np.maximum(delta, 0)
            lo = np.maximum.reduce([np.zeros(samples), a - b, -delta])
            hi = np.minimum.reduce([a, q, np.where(delta >= 0, a, d) - eta])
            linear = ((b - d) * (c - a) + (p - a) * delta
                      - 2 * a * q + (a + q) * eta)
            t = np.minimum(hi, np.maximum(lo, -linear / (2 * np.minimum(a + c, b + d))))
            cuts = (t, a - t, p + t, q - t)
            volumes, widths = [], []
            local_lengths = (a, b, c, d)
            for i in range(4):
                j = (i + 1) % 4
                x, y = local_lengths[i], local_lengths[j]
                u, v = cuts[i], cuts[j]
                volumes.append(x * y - u * (y - v))
                widths.append(np.maximum(np.minimum(x, v), np.minimum(x - u, y)))
            cost = sum(volumes[i] * widths[i + 2] + widths[i] * volumes[i + 2]
                       for i in range(2)) / volume
            best = np.minimum(best, np.where(lo <= hi, cost, np.inf))
    scale = sqrt(pi / 2)
    saving = scale * (baseline - best)
    print(f"balanced menu: samples={samples} mean={scale*np.mean(best):.10f} "
          f"SE={scale*np.std(best)/sqrt(samples):.10f}")
    print(f"paired mean saving={np.mean(saving):.10f}; "
          f"saving SE={np.std(saving)/sqrt(samples):.10f}; "
          f"switched={np.mean(saving > 1e-10):.8f}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=int, default=0)
    parser.add_argument("--divisions", type=int, default=4)
    parser.add_argument("--seed", type=int, default=906621)
    parser.add_argument("--passes", type=int, default=0)
    parser.add_argument("--balanced", action="store_true")
    args = parser.parse_args()
    if args.samples:
        if args.balanced:
            numerical_balanced(args.samples, args.seed)
        else:
            numerical(args.samples, args.divisions, args.seed, args.passes)
    else:
        audit()
