"""Exact checks for the three-accumulator pi^2/8 upper bound.

No stochastic estimate or numerical quadrature is used. Run with -B.
All mathematical assertions use integers or fractions. Seeded integer
invariant tests corroborate, rather than replace, the pathwise proof.
Decimal printing only presents rational enclosures proved by assertions.
"""

from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations_with_replacement, product
from math import prod
from random import Random


def scd(bits):
    result = [(0,)]
    for bit in bits:
        following = []
        for chain in result:
            following.append(chain + (chain[-1] | bit,))
            if len(chain) > 1:
                following.append(tuple(x | bit for x in chain[:-1]))
        result = following
    return result


def hook(left, right):
    if len(left) > len(right):
        left, right = right, left
    for j in range(len(left)):
        corner = len(left) - 1 - j
        yield (tuple(left[i] | right[j] for i in range(corner + 1))
               + tuple(left[corner] | right[i] for i in range(j + 1, len(right))))


@lru_cache(None)
def bridge(support, chain):
    return tuple(x for x in (chain[0],)
                 + tuple(b ^ a for a, b in zip(chain, chain[1:]))
                 + (support ^ chain[-1],) if x)


def unions(word):
    ending, seen = set(), set()
    for letter in word:
        ending = {letter} | {x | letter for x in ending}
        seen.update(ending)
    return seen


def child_lengths(a, b):
    return range(abs(a - b) + 1, a + b, 2)


@lru_cache(None)
def charge(active, unread):
    a, b, c = active
    assert a <= b <= c
    if not unread:
        return a * (b + c)
    return sum(charge(tuple(sorted((r, b, c))), unread[1:])
               for r in child_lengths(a, unread[0]))


@lru_cache(None)
def weighted_cost(active, unread):
    a, b, c = active
    if not unread:
        return 1 / F(b) + 1 / F(c)
    d = unread[0]
    return sum((F(r, a * d) * weighted_cost(tuple(sorted((r, b, c))), unread[1:])
                for r in child_lengths(a, d)), F(0))


def leaves(active, unread):
    if not unread:
        i, j, fixed = sorted(range(3), key=lambda t: (len(active[t][1]), t))
        support = active[i][0] | active[j][0]
        for chain in hook(active[i][1], active[j][1]):
            yield (support, chain), active[fixed]
        return
    i = min(range(3), key=lambda t: (len(active[t][1]), t))
    support = active[i][0] | unread[0][0]
    for chain in hook(active[i][1], unread[0][1]):
        following = list(active)
        following[i] = (support, chain)
        yield from leaves(tuple(following), unread[1:])


def compile_cube(sizes):
    universes, decompositions = [], []
    k = 0
    for size in sizes:
        universes.append(((1 << size) - 1) << k)
        decompositions.append(scd(tuple(1 << j for j in range(k, k + size - 1))))
        k += size
    full = (1 << k) - 1
    adjacency, partition = {}, set()
    edge_count = main_cost = predicted = boundary_count = 0
    for chains in product(*decompositions):
        lengths = tuple(map(len, chains))
        predicted += (1 << (len(chains) - 1)) * charge(tuple(sorted(lengths[:3])), lengths[3:])
        for signs in product((0, 1), repeat=len(sizes) - 1):
            factors = tuple((u, chain if sign == 0 else tuple(u ^ x for x in reversed(chain)))
                            for u, chain, sign in zip(universes, chains, (0,) + signs))
            for left, desired_right in leaves(factors[:3], factors[3:]):
                if not left[0] & universes[0]:
                    left, desired_right = desired_right, left
                right = (desired_right[0], tuple(desired_right[0] ^ x
                                                 for x in reversed(desired_right[1])))
                assert left[0] & right[0] == 0 and left[0] | right[0] == full
                wanted = {a | b for a in left[1] for b in desired_right[1]}
                complements = {full ^ x for x in wanted}
                assert not wanted & complements
                assert not partition & (wanted | complements)
                partition.update(wanted | complements)
                lb, rb = bridge(*left), bridge(*right)
                assert wanted - {0} <= unions(rb + lb)
                assert complements - {0} <= unions(lb + rb)
                boundary_count += 2
                for support, chain in (left, right):
                    assert all(a & b == a and (b ^ a).bit_count() == 1
                               for a, b in zip(chain, chain[1:]))
                    assert len(chain) <= len(bridge(support, chain)) <= len(chain) + 1
                adjacency.setdefault(left, []).append(right)
                adjacency.setdefault(right, []).append(left)
                edge_count += 1
                main_cost += len(left[1]) + len(right[1])
    assert partition == set(range(full + 1))
    assert main_cost == predicted
    word = []
    primary = closing = components = arcs = 0
    for root in adjacency:
        if not adjacency[root]:
            continue
        stack, circuit = [root], []
        while stack:
            if adjacency[stack[-1]]:
                stack.append(adjacency[stack[-1]].pop())
            else:
                circuit.append(stack.pop())
        circuit.reverse()
        assert circuit[0] == circuit[-1] == root
        for vertex in circuit[:-1]:
            word.extend(bridge(*vertex))
            primary += len(bridge(*vertex))
            arcs += 1
        word.extend(bridge(*root))
        closing += len(bridge(*root))
        components += 1
    assert arcs == 2 * edge_count
    assert main_cost <= primary <= main_cost + 2 * edge_count
    assert closing <= (k + 1) * components <= (k + 1) * len(adjacency)
    assert len(word) == primary + closing
    assert all(0 < x <= full for x in word)
    assert unions(word) == set(range(1, full + 1))
    return (len(word), main_cost, primary - main_cost, closing,
            edge_count, len(adjacency), components, boundary_count)


def rational_certificate():
    def atan_bounds(x):
        lower = sum(((-1) ** j * x ** (2 * j + 1) / (2 * j + 1)
                     for j in range(40)), F(0))
        return lower, lower + x ** 81 / 81

    al, au = atan_bounds(F(1, 5))
    bl, bu = atan_bounds(F(1, 239))
    pl, pu = 16 * al - 4 * bu, 16 * au - 4 * bl
    lower, upper = pl * pl / 8, pu * pu / 8
    assert F(1233700, 10**6) < lower < upper < F(1233701, 10**6)
    assert pu / 8 < F(627, 1000) ** 2 < 1
    m, epsilon = 2**30, F(1, 2**10)
    assert m * epsilon**2 / 6 > 170
    power = (1 / (72 * epsilon**2)).numerator // (1 / (72 * epsilon**2)).denominator
    assert power == 14563
    d_upper = F(36 * m, 2**170) + F(3, 2**power)
    assert d_upper < F(1, 2**133)
    assert 12 * m < 2**34
    finite_upper = F(1233701, 10**6) + F(627, 1000) * 10 * epsilon + F(1, 2**49)
    assert finite_upper < F(1239825, 10**6) < F(124, 100)
    return lower, upper, finite_upper


def recurrence_checks():
    count = 0
    for a, b in product(range(1, 41), repeat=2):
        children = tuple(child_lengths(a, b))
        assert sum(children) == a * b
        assert len(children) == min(a, b)
        for c in (1, 7, 23):
            if a <= b <= c:
                assert sum(r + c for r in children) == a * (b + c)
    for active in combinations_with_replacement(range(1, 6), 3):
        for unread_size in range(5):
            for unread in product(range(1, 5), repeat=unread_size):
                value = charge(active, unread)
                volume = prod(active + unread)
                assert F(value, volume) == weighted_cost(active, unread)
                assert value <= sum(volume // a for a in active + unread)
                count += 1
    return count


def clock_invariant_checks():
    rng = Random(20260906)
    count = 0
    for bound in range(1, 8):
        for _ in range(100):
            current, historic = [0, 0, 0], [0, 0, 0]
            previous_second = 0
            for _ in range(200):
                i = min(range(3), key=lambda j: (current[j], j))
                following = max(0, current[i] + rng.randrange(-bound, bound + 1))
                assert abs(following - current[i]) <= bound
                current[i] = following
                historic[i] = max(historic[i], following)
                _, second, largest = sorted(current)
                assert largest == max(historic)
                assert second >= previous_second
                assert largest - second <= bound
                assert all(largest - bound <= h <= largest for h in historic)
                previous_second = second
                count += 1
    return count


def main():
    lo, hi, finite = rational_certificate()
    print(f"Exact-rational pi^2/8 enclosure: {float(lo):.15f} .. {float(hi):.15f}")
    print(f"Exact-rational fixed m=2^30 upper certificate: {float(finite):.15f} < 1.239825")
    print(f"Exact volume-weighted recurrence checks: {recurrence_checks()}")
    print(f"Exact minimum-update invariant checks: {clock_invariant_checks()}")
    for sizes in ((2, 2, 2), (2, 2, 2, 2), (2, 3, 2, 3, 2),
                  (2, 2, 2, 2, 2, 2), (3, 3, 3, 3, 3), (2,) * 8):
        n, main_cost, endpoints, closing, edges, vertices, components, boundaries = compile_cube(sizes)
        print(f"Literal word blocks={sizes}: length={n}, main={main_cost}, "
              f"endpoints={endpoints}, closing={closing}, edges={edges}, "
              f"vertices={vertices}, components={components}, boundaries={boundaries}")
    print("All exact assertions passed; no probabilistic confidence bounds were used.")


if __name__ == "__main__":
    main()
