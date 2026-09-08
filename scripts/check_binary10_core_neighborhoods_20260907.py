"""Literal check of the core-neighborhood lemma; execute via ssh h100 only."""

import importlib.util
import os
from itertools import combinations
from pathlib import Path
import sys


def load_core(path):
    spec = importlib.util.spec_from_file_location("binary10_core", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def all_matchings(lower):
    upper = [x for x in range(32) if x.bit_count() == 3]
    options = [[b for b in upper if a & b == a] for a in lower]

    def visit(chosen, used):
        if len(chosen) == len(lower):
            yield chosen
        else:
            for b in options[len(chosen)]:
                if b not in used:
                    yield from visit(chosen + [b], used | {b})

    yield from visit([], set())


def transversal(signs):
    return sum(1 << (i + 5 * ((signs >> i) & 1)) for i in range(5))


def main(core_path):
    core = load_core(core_path)
    lower = [sum(1 << i for i in a) for a in combinations(range(5), 2)]
    matchings = list(all_matchings(lower))
    assert len(matchings) == 60
    cores = transversal_cases = upper_cases = 0
    for mode in ("increasing", "regular"):
        os.environ["BINARY10_CORE_FIRST_ORDER"] = mode
        for upper in matchings:
            rows = core.build_core(lower, upper)
            covered = set.union(*(core.row_support(row) for row in rows))
            arrows = {(row[0][0] % 5, row[0][1] % 5) for row in rows}
            last = {a: row[0][-1] % 5 for a, row in zip(lower, rows)}
            indegree = [sum(v == i for u, v in arrows) for i in range(5)]
            outdegree = [sum(u == i for u, v in arrows) for i in range(5)]
            if mode == "regular":
                assert indegree == outdegree == [2] * 5
            actual = {z for z in range(32) if transversal(z) in covered}
            assert actual == {z for z in range(32) if z.bit_count() in (2, 3)}

            for exceptional in [None] + list(range(5)):
                target = transversal(0 if exceptional is None else 1 << exceptional)
                assert target not in covered
                lower_neighbors = [target ^ (1 << i) for i in range(10)
                                   if target >> i & 1]
                upper_neighbors = [target | (1 << i) for i in range(10)
                                   if not (target >> i & 1)]
                assert len(lower_neighbors) == len(upper_neighbors) == 5
                assert not any(x in covered for x in lower_neighbors)
                expected = 0 if exceptional is None else indegree[exceptional]
                assert sum(x in covered for x in upper_neighbors) == expected
                transversal_cases += 1

            for doubled in range(5):
                rest = set(range(5)) - {doubled}
                for sign_tuple in combinations(sorted(rest), 2):
                    signs = set(sign_tuple)
                    target = transversal(sum(1 << i for i in signs))
                    target |= 1 << (doubled + 5)
                    assert target.bit_count() == 6 and target not in covered
                    assert target ^ (1 << doubled) in covered
                    assert target ^ (1 << (doubled + 5)) in covered
                    free = 0
                    for removed in rest:
                        part = signs if removed in signs else rest - signs
                        partner = next(iter(part - {removed}))
                        owner = (1 << doubled) | (1 << partner)
                        expected = ((doubled, partner) in arrows
                                    and last[owner] == removed)
                        bit = removed + (5 if removed in signs else 0)
                        predecessor = target ^ (1 << bit)
                        assert (predecessor in covered) == expected
                        free += predecessor not in covered
                    assert free >= 4 - outdegree[doubled]
                    if mode == "regular":
                        assert free >= 2
                    upper_cases += 1
            cores += 1
    print("PASS", cores, "literal cores;", transversal_cases,
          "transversal neighborhoods;", upper_cases, "rank-six neighborhoods")


if __name__ == "__main__":
    default = (Path(__file__).resolve().parents[1] / "scratch"
               / "binary10_involution_matching_core_20260907.py")
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else default)
