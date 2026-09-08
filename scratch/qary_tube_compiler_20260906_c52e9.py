"""Explicit cube-tube chain partitions and literal lifted template words."""

from itertools import product
from random import Random
from fractions import Fraction


def tube_width_factor(chain):
    """Exact leading factor in dimensions <=3; the upper bound 1 otherwise."""
    if len(chain[0]) != 3:
        return Fraction(1)
    longest, run, previous = 1, 0, None
    for x, y in zip(chain, chain[1:]):
        mask = sum(1 << i for i in range(3) if x[i] != y[i])
        if mask.bit_count() == 1:
            return Fraction(1)
        if mask.bit_count() == 3:
            run, previous = 0, None
        else:
            run = run + 1 if previous == mask else 1
            previous = mask
            longest = max(longest, run + 1)
    return Fraction(3, 4) if longest == 1 else 1 - Fraction(1, 4 * longest)


def optimal_three_tube(chain, q, m):
    """Actual minimum chain partition, by bipartite matching, with a width check."""
    assert len(chain[0]) == 3
    assert q >= 2 and m >= 1
    assert all(all(0 <= x < q for x in p) for p in chain)
    assert all(x != y and all(a <= b for a, b in zip(x, y))
               for x, y in zip(chain, chain[1:]))
    points = sorted({tuple(m * x + y for x, y in zip(p, micro))
                     for p in chain for micro in product(range(m), repeat=3)})
    edges = [[j for j in range(i + 1, len(points))
              if all(a <= b for a, b in zip(x, points[j]))]
             for i, x in enumerate(points)]
    matched = [-1] * len(points)

    def augment(i, visited):
        for j in edges[i]:
            if visited[j]:
                continue
            visited[j] = True
            if matched[j] < 0 or augment(matched[j], visited):
                matched[j] = i
                return True
        return False

    for i in range(len(points)):
        augment(i, [False] * len(points))
    successor = {i: j for j, i in enumerate(matched) if i >= 0}
    chains = []
    for start, predecessor in enumerate(matched):
        if predecessor >= 0:
            continue
        current, part = start, []
        while True:
            part.append(points[current])
            if current not in successor:
                break
            current = successor[current]
        chains.append(part)
    factor = tube_width_factor(chain)
    if factor == 1:
        expected = m * m
    elif factor == Fraction(3, 4):
        expected = m * m - (m * m) // 4
    else:
        length = int(1 / (4 * (1 - factor)))
        expected = sum(min(m, length * (2 * m - 1 - 2 * j)) for j in range(m))
    assert len(chains) == expected
    assert sum(map(len, chains)) == len(chain) * m ** 3
    return chains


def tube_chains(chain, q, m):
    """Partition the m-cube blow-up of a strict chain into m**(d-1) chains."""
    d = len(chain[0])
    assert q >= 2 and m >= 1 and chain
    assert all(all(0 <= x < q for x in p) for p in chain)
    assert all(x != y and all(a <= b for a, b in zip(x, y))
               for x, y in zip(chain, chain[1:]))
    # Complete to a saturated path. The omitted cells are removed at the end.
    path = [(0,) * d]
    for target in list(chain) + [(q - 1,) * d]:
        current = list(path[-1])
        for axis in range(d):
            while current[axis] < target[axis]:
                current[axis] += 1
                path.append(tuple(current))
        assert tuple(current) == target
    steps = [next(i for i in range(d) if x[i] != y[i])
             for x, y in zip(path, path[1:])]
    keep = set(chain)
    output, exits = [], {}
    for position, cell in enumerate(path):
        incoming = steps[position - 1] if position else steps[0]
        outgoing = steps[position] if position < len(steps) else steps[-1]
        fixed = [i for i in range(d) if i not in (incoming, outgoing)]
        pieces = []
        for values in product(range(m), repeat=len(fixed)):
            base = [0] * d
            for i, value in zip(fixed, values):
                base[i] = value
            if incoming == outgoing:
                piece = []
                for value in range(m):
                    point = base.copy()
                    point[incoming] = value
                    piece.append(tuple(point))
                pieces.append(piece)
            else:
                for j in range(m):
                    pairs = ([(x, j) for x in range(m - j)]
                             + [(m - 1 - j, y) for y in range(j + 1, m)])
                    piece = []
                    for x, y in pairs:
                        point = base.copy()
                        point[incoming], point[outgoing] = x, y
                        piece.append(tuple(point))
                    pieces.append(piece)
        following = {}
        for piece in pieces:
            if position == 0:
                owner = len(output)
                output.append([])
            else:
                before = list(piece[0])
                before[incoming] = m - 1
                owner = exits[tuple(before)]
            if cell in keep:
                output[owner].extend(tuple(m * a + b for a, b in zip(cell, point))
                                     for point in piece)
            end = piece[-1]
            assert end not in following
            following[end] = owner
        assert len(following) == m ** (d - 1)
        exits = following
    assert len(output) == m ** (d - 1) and all(output)
    assert sum(map(len, output)) == len(chain) * m ** d
    return output


def bridge(chain, support):
    word = [chain[0]]
    word.extend(y & ~x for x, y in zip(chain, chain[1:]))
    word.append(support & ~chain[-1])
    return [x for x in word if x]


def word_unions(word):
    unions, suffixes = set(), set()
    for letter in word:
        assert letter
        suffixes = {letter} | {x | letter for x in suffixes}
        unions.update(suffixes)
    return unions


def lifted_word(template, q, dimension, m, optimal_three=False):
    """Rows have (left support, left index chain, right support, right chain)."""
    a = q * m
    factors, supports = [], []
    offset = 0
    for _ in range(dimension):
        current = 1 << offset
        offset += 1
        chain = [current]
        for _ in range(a - 1):
            current |= 1 << offset
            offset += 1
            chain.append(current)
        current |= 1 << offset
        offset += 1
        factors.append(chain)
        supports.append(current)
    full = sum(supports)
    adjacency, vertex_words = {}, {}
    charge, edges, expected_charge, expected_edges = 0, 0, 0, 0
    for left, c, right, d in template:
        assert sorted(left + right) == list(range(dimension))
        assert left and right
        cc = optimal_three_tube(c, q, m) if optimal_three and len(left) == 3 else tube_chains(c, q, m)
        dd = optimal_three_tube(d, q, m) if optimal_three and len(right) == 3 else tube_chains(d, q, m)
        expected_charge += len(c) * m ** len(left) * len(dd) + len(d) * m ** len(right) * len(cc)
        expected_edges += len(cc) * len(dd)

        def encode(path, axes):
            out = []
            for point in path:
                value = 0
                for i, x in zip(axes, point):
                    value |= factors[i][x]
                out.append(value)
            return tuple(out)

        u, v = sum(supports[i] for i in left), sum(supports[i] for i in right)
        for e, f in product(cc, dd):
            csets, dsets = encode(e, left), encode(f, right)
            dc = tuple(v ^ x for x in reversed(dsets))
            source, target = (u, csets), (v, dc)
            vertex_words[source] = bridge(csets, u)
            vertex_words[target] = bridge(dc, v)
            adjacency.setdefault(source, []).append(target)
            adjacency.setdefault(target, []).append(source)
            charge += len(csets) + len(dsets)
            edges += 1
    coarse_charge = sum(len(c) + len(d) for _, c, _, d in template)
    assert charge == expected_charge and edges == expected_edges
    if not optimal_three:
        assert charge == coarse_charge * m ** (dimension - 1)
        assert edges == len(template) * m ** (dimension - 2)
    word, principal_positions, closing_positions = [], 0, 0
    components = 0
    for start in list(adjacency):
        if not adjacency[start]:
            continue
        components += 1
        stack, tour = [start], []
        while stack:
            current = stack[-1]
            if adjacency[current]:
                stack.append(adjacency[current].pop())
            else:
                tour.append(stack.pop())
        tour.reverse()
        assert tour[0] == tour[-1]
        for vertex in tour[:-1]:
            word.extend(vertex_words[vertex])
            principal_positions += len(vertex_words[vertex])
        word.extend(vertex_words[tour[-1]])
        closing_positions += len(vertex_words[tour[-1]])
    assert principal_positions <= charge + 2 * edges
    assert components <= len(template)
    assert closing_positions <= components * (dimension * a + 2)
    assert len(word) == principal_positions + closing_positions
    required = set()
    for values in product(*factors):
        target = 0
        for value in values:
            target |= value
        required.update((target, full ^ target))
    assert required <= word_unions(word)
    return len(word), charge, edges, len(required)


def audit():
    rng = Random(906529)
    cases, width_cases = 0, 0
    for d in range(1, 6):
        for q in range(2, 5):
            for m in range(1, 4):
                for _ in range(8):
                    moves = [i for i in range(d) for _ in range(q - 1)]
                    rng.shuffle(moves)
                    path = [(0,) * d]
                    for i in moves:
                        current = list(path[-1])
                        current[i] += 1
                        path.append(tuple(current))
                    chosen = [p for p in path if rng.randrange(3)] or [path[len(path) // 2]]
                    lifted = tube_chains(chosen, q, m)
                    assert all(all(x != y and all(a <= b for a, b in zip(x, y))
                                   for x, y in zip(c, c[1:])) for c in lifted)
                    expected = {tuple(m * x + y for x, y in zip(p, micro))
                                for p in chosen for micro in product(range(m), repeat=d)}
                    flat = [p for c in lifted for p in c]
                    assert len(flat) == len(set(flat)) and set(flat) == expected
                    if d == 3:
                        optimal_three_tube(chosen, q, m)
                        width_cases += 1
                    cases += 1
    binary = [((0, 1), ((0, 0), (1, 0), (1, 1)),
               (2, 3), ((0, 0), (1, 0), (1, 1))),
              ((1, 2), ((0, 0), (1, 0), (1, 1)),
               (3, 0), ((0, 0), (1, 0), (1, 1)))]
    for m in (1, 2, 3, 4):
        result = lifted_word(binary, 2, 4, m)
        assert result[1] == 12 * m ** 3
        print(f"literal binary template, m={m}: length, charge, edges, targets={result}")
    # A genuinely ternary template: a full-grid SCD on two shores.
    q = 3
    planar = []
    for j in range(q):
        planar.append(tuple([(x, j) for x in range(q - j)]
                            + [(q - 1 - j, y) for y in range(j + 1, q)]))
    ternary = [((0, 1), c, (2, 3), d) for c, d in product(planar, repeat=2)]
    for m in (1, 2, 3):
        print(f"literal ternary template, m={m}: "
              f"length, charge, edges, targets={lifted_word(ternary, 3, 4, m)}")
    singleton_template = [((0, 1, 2), (x,), (3, 4, 5), (y,))
                          for x, y in product(product(range(2), repeat=3), repeat=2)]
    for m in (2, 3):
        result = lifted_word(singleton_template, 2, 6, m, optimal_three=True)
        assert result[1] == 128 * m ** 3 * (m * m - m * m // 4)
        print(f"optimal-width six-axis tube word, m={m}: {result}")
    print(f"PASS {cases} exact tube partitions, {width_cases} minimum-width checks, "
          "and nine literal paired-box words")


if __name__ == "__main__":
    audit()
