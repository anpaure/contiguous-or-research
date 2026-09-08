"""Build a ten-row invariant tight-palette core, not a full cube cover."""

from itertools import product


def scd(n):
    chains = [[0]]
    for bit in range(n):
        flag = 1 << bit
        following = []
        for chain in chains:
            following.append(chain + [chain[-1] | flag])
            if len(chain) > 1:
                following.append([x | flag for x in chain[:-1]])
        chains = following
    return chains


def extend(chain, n):
    order = [i for i in range(n) if chain[0] >> i & 1]
    order += [(b ^ a).bit_length()-1 for a, b in zip(chain, chain[1:])]
    order += [i for i in range(n) if not (chain[-1] >> i & 1)]
    assert sorted(order) == list(range(n))
    return order


def prefixes(order):
    out = [0]
    for x in order:
        out.append(out[-1] | (1 << x))
    return out


def involution(mask):
    return ((mask & 31) << 5) | (mask >> 5)


def main():
    orders = [extend(chain, 5) for chain in scd(5)]
    assert len(orders) == 10
    candidates = []
    for order in orders:
        choices = []
        for signs in range(16):
            left = [i+5*((signs >> i) & 1) for i in order]
            right = [i+5*(1-((signs >> i) & 1)) for i in order]
            support = {x | y for x, y in product(prefixes(left), prefixes(right))}
            assert {involution(x) for x in support} == support
            tight = frozenset(x for x in support if 4 <= x.bit_count() <= 6)
            assert len(tight) == 16
            choices.append((left, right, support, tight))
        candidates.append(choices)

    def search(todo, used, selected):
        if not todo:
            return selected
        choices_by_id = [(i, [r for r in candidates[i] if not (r[3] & used)])
                         for i in todo]
        i, choices = min(choices_by_id, key=lambda item: len(item[1]))
        for row in choices:
            result = search([j for j in todo if j != i], used | row[3], selected+[(i,row)])
            if result is not None:
                return result
        return None

    result = search(list(range(10)), frozenset(), [])
    if result is None:
        print("No sign assignment for these prescribed SCD extensions.")
        return
    support = set()
    for i, (left,right,row,tight) in sorted(result):
        print(" ".join(map(str,left)), "|", " ".join(map(str,right)))
        support |= row
    required_fixed = {x for x in range(1024)
                      if involution(x) == x and 4 <= x.bit_count() <= 6}
    assert required_fixed <= support
    print("PASS ten invariant rows, 160 distinct tight targets, all 20 fixed tight targets")
    print("full-cube coverage", len(support), "of 1024")
    print("rank counts", [sum(x.bit_count() == r for x in support) for r in range(11)])


if __name__ == "__main__":
    main()
