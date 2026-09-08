"""Generate a tight-disjoint invariant core for a prescribed fixed matching.

The three representatives are the three S5-orbits of perfect matchings between
the rank-2 and rank-3 levels of B_5. A degree-two conflict graph gives a core
without search, for any such perfect matching. This is not a full-cube solver.
Run verification only on ssh h100 under the project's compute policy.
"""

import os
import sys
from itertools import combinations, product


MATCHINGS = {
    "6": (7, 13, 25, 19, 22, 11, 26, 14, 21, 28),
    "24": (7, 13, 11, 19, 14, 26, 22, 28, 21, 25),
    "30": (7, 13, 11, 19, 22, 14, 26, 28, 21, 25),
}


def all_fixed_matchings():
    lower = [sum(1 << i for i in labels) for labels in combinations(range(5), 2)]
    upper = [x for x in range(32) if x.bit_count() == 3]
    options = [[b for b in upper if a & b == a] for a in lower]
    result = []

    def visit(chosen, used):
        if len(chosen) == 10:
            result.append(tuple(chosen))
            return
        for b in options[len(chosen)]:
            if b not in used:
                visit(chosen + [b], used | {b})

    visit([], set())
    assert len(result) == 60
    return lower, result


def prefixes(order):
    ans = [0]
    for label in order:
        ans.append(ans[-1] | (1 << label))
    return ans


def row_support(row):
    return {x | y for x, y in product(*(prefixes(order) for order in row))}


def last_assignments(lower, upper):
    """All valid last-label assignments, canonical previous choice first."""
    assert len(lower) == len(upper) == 10
    assert len(set(lower)) == len(set(upper)) == 10
    assert all(a.bit_count() == 2 and b.bit_count() == 3 and a & b == a
               for a, b in zip(lower, upper))
    lookup = {a: i for i, a in enumerate(lower)}
    choices = [{j for j in range(5) if not (b >> j & 1)} for b in upper]
    neighbors = [{} for _ in lower]
    for i, a in enumerate(lower):
        for j in choices[i]:
            partner = lookup[31 ^ (1 << j) ^ a]
            if j in choices[partner]:
                neighbors[i][partner] = j
    assert all(len(n) <= 2 for n in neighbors)

    factors = []
    unseen = set(range(10))
    while unseen:
        component, pending = set(), [min(unseen)]
        while pending:
            i = pending.pop()
            if i in component:
                continue
            component.add(i)
            pending.extend(neighbors[i])
        unseen -= component
        endpoints = sorted(i for i in component if len(neighbors[i]) < 2)
        start = endpoints[0] if endpoints else min(component)
        previous, current = None, start
        order = [start]
        while True:
            following = [i for i in sorted(neighbors[current]) if i != previous]
            if not following:
                break
            nxt = following[0]
            if nxt == start:
                break
            order.append(nxt)
            previous, current = current, nxt
        options = []
        if endpoints:
            # On a path the choices must be all left, then all right: a
            # right-then-left pair would select one edge at both ends.
            for left_count in range(len(order), -1, -1):
                selected = {}
                for position, i in enumerate(order):
                    if position < left_count:
                        selected[i] = (neighbors[i][order[position-1]] if position
                                       else min(choices[i] - set(neighbors[i].values())))
                    else:
                        selected[i] = (neighbors[i][order[position+1]]
                                       if position+1 < len(order)
                                       else max(choices[i] - set(neighbors[i].values())))
                options.append(selected)
        else:
            for step in (1, -1):
                options.append({i: neighbors[i][order[(position+step) % len(order)]]
                                for position, i in enumerate(order)})
        factors.append(options)
    assignments = []
    for component_choices in product(*factors):
        selected = {i: label for choice in component_choices for i, label in choice.items()}
        assert len(selected) == 10
        for i, neighbors_i in enumerate(neighbors):
            for partner, label in neighbors_i.items():
                assert not (selected[i] == selected[partner] == label)
        assignments.append(selected)
    return assignments


def build_core(lower, upper, last_variant=None):
    """Construct ten rows; the input is any rank-2/rank-3 perfect matching."""
    assignments = last_assignments(lower, upper)
    if last_variant is None:
        last_variant = int(os.environ.get("BINARY10_LAST_VARIANT", "0"))
    if not 0 <= last_variant < len(assignments):
        raise ValueError(f"Last variant must be between 0 and {len(assignments)-1}")
    selected = assignments[last_variant]
    choices = [{j for j in range(5) if not (b >> j & 1)} for b in upper]

    rows = []
    for i, (a, b) in enumerate(zip(lower, upper)):
        first = [j for j in range(5) if a >> j & 1]
        # The regular five-vertex tournament avoids the artificial sink
        # obstruction caused by always putting the smaller label first.
        first_order = os.environ.get("BINARY10_CORE_FIRST_ORDER", "regular")
        if first_order not in ("regular", "increasing"):
            raise ValueError("BINARY10_CORE_FIRST_ORDER must be regular or increasing")
        if first_order == "regular" and (first[1] - first[0]) % 5 not in (1, 2):
            first.reverse()
        middle = (b ^ a).bit_length() - 1
        last = selected[i]
        penultimate = next(j for j in choices[i] if j != last)
        order = first + [middle, penultimate, last]
        left = tuple(j + 5 * ((a >> j) & 1) for j in order)
        right = tuple(j + 5 * (1 - ((a >> j) & 1)) for j in order)
        rows.append((left, right))
    return rows


def main():
    name = os.environ.get("BINARY10_FIXED_MATCHING", "6")
    lower, matchings = all_fixed_matchings()
    if "BINARY10_MATCHING_INDEX" in os.environ:
        index = int(os.environ["BINARY10_MATCHING_INDEX"])
        if not 0 <= index < len(matchings):
            raise ValueError("BINARY10_MATCHING_INDEX must be between 0 and 59")
        name = f"index:{index}"
        upper = matchings[index]
    else:
        if name not in MATCHINGS:
            raise ValueError("BINARY10_FIXED_MATCHING must be 6, 24, or 30")
        upper = MATCHINGS[name]
    assert len(set(upper)) == 10
    assert all(a & b == a and b.bit_count() == 3 for a, b in zip(lower, upper))

    rows = build_core(lower, upper)
    total = set()
    for row in rows:
        support = row_support(row)
        print(" ".join(map(str, row[0])), "|", " ".join(map(str, row[1])))
        total |= support
    assert sum(4 <= x.bit_count() <= 6 for x in total) == 160
    fixed_tight = {x | (x << 5) for x in range(32) if x.bit_count() in (2, 3)}
    assert fixed_tight <= total
    print("PASS_FIXED_MATCHING", name, "coverage", len(total))
    print("rank counts", [sum(x.bit_count() == r for x in total) for r in range(11)])


def verify_all(all_variants=False):
    lower, matchings = all_fixed_matchings()
    count = 0
    for chosen in matchings:
        variants = range(len(last_assignments(lower, chosen))) if all_variants else [0]
        for variant in variants:
            rows = build_core(lower, chosen, variant)
            supports = [row_support(row) for row in rows]
            tight = [{x for x in support if 4 <= x.bit_count() <= 6}
                     for support in supports]
            assert all(len(t) == 16 for t in tight)
            assert len(set.union(*tight)) == 160
            fixed = {x | (x << 5) for x in range(32) if x.bit_count() in (2, 3)}
            assert fixed <= set.union(*supports)
            count += 1

    assert count == (10176 if all_variants else 60)
    print("PASS all 60 fixed matchings:", count,
          "literal ten-row cores, 160 distinct tight targets")


if __name__ == "__main__":
    if sys.argv[1:] == ["--verify-all"]:
        verify_all()
    elif sys.argv[1:] == ["--verify-all-variants"]:
        verify_all(True)
    elif not sys.argv[1:]:
        main()
    else:
        raise SystemExit("usage: script.py [--verify-all | --verify-all-variants]")
